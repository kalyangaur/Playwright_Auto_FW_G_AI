import os
import pytest
import allure
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from config.config import settings
from core.driver_factory import DriverFactory
from core.logger import logger
from utils.allure_helper import AllureHelper


def pytest_addoption(parser):
    """Register custom CLI options if not already registered by installed plugins."""
    try:
        parser.addoption(
            "--browser-type",
            action="store",
            default=None,
            help="Target browser: chromium, firefox, webkit",
        )
    except Exception:
        pass

    try:
        parser.addoption(
            "--headed",
            action="store_true",
            default=False,
            help="Run browser in headed mode",
        )
    except Exception:
        pass



@pytest.fixture(scope="session")
def browser_name_cli(request):
    cli_browser = request.config.getoption("--browser-type")
    return cli_browser if cli_browser else settings.browser


@pytest.fixture(scope="session")
def headed_cli(request):
    is_headed = request.config.getoption("--headed")
    if is_headed:
        settings.headless = False
    return not settings.headless


@pytest.fixture(scope="session")
def playwright_instance():
    """Session-scoped Playwright instance."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright, browser_name_cli: str) -> Browser:
    """Session-scoped Browser instance."""
    browser = DriverFactory.create_browser(playwright_instance, browser_name_cli)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser, request) -> BrowserContext:
    """Function-scoped BrowserContext with isolated storage and optional video/trace."""
    record_video = settings.video in ("on", "retain-on-failure")
    context = DriverFactory.create_context(browser, record_video=record_video)
    yield context
    
    # Save trace on failure if configured
    test_failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    if settings.trace in ("on", "retain-on-failure") and (test_failed or settings.trace == "on"):
        traces_dir = "reports/traces"
        os.makedirs(traces_dir, exist_ok=True)
        trace_path = os.path.join(traces_dir, f"{request.node.name}_trace.zip")
        context.tracing.stop(path=trace_path)
        if os.path.exists(trace_path):
            allure.attach.file(trace_path, name="Playwright Trace", extension="zip")
    else:
        try:
            context.tracing.stop()
        except Exception:
            pass

    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext, request) -> Page:
    """Function-scoped Page instance."""
    page = DriverFactory.create_page(context)
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture test execution status and take screenshots on failure."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        # Test failed; try to capture screenshot from page fixture
        page_instance = item.funcargs.get("page")
        if page_instance:
            try:
                screenshot_bytes = page_instance.screenshot(full_page=True)
                AllureHelper.attach_screenshot(
                    screenshot_bytes,
                    name=f"Failure_Screenshot_{item.name}",
                )
                html_content = page_instance.content()
                AllureHelper.attach_html(
                    html_content,
                    name=f"Failure_DOM_{item.name}",
                )
            except Exception as e:
                logger.error(f"Failed to capture screenshot/DOM on failure: {e}")
