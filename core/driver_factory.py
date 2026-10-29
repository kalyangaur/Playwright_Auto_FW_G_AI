from typing import Optional
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from config.config import settings
from core.logger import logger


class DriverFactory:
    """Factory responsible for instantiating Playwright browsers, contexts, and pages."""

    @staticmethod
    def create_browser(playwright: Playwright, browser_name: Optional[str] = None) -> Browser:
        browser_type = (browser_name or settings.browser).lower()
        logger.info(f"Initializing browser: {browser_type} (headless={settings.headless})")

        launch_args = ["--start-maximized", "--disable-notifications"]
        
        if browser_type == "firefox":
            return playwright.firefox.launch(
                headless=settings.headless,
                slow_mo=settings.slow_mo,
            )
        elif browser_type == "webkit":
            return playwright.webkit.launch(
                headless=settings.headless,
                slow_mo=settings.slow_mo,
            )
        else:  # default chromium
            return playwright.chromium.launch(
                headless=settings.headless,
                slow_mo=settings.slow_mo,
                args=launch_args,
            )

    @staticmethod
    def create_context(
        browser: Browser,
        record_video: bool = False,
        video_dir: str = "reports/videos",
    ) -> BrowserContext:
        context_kwargs = {
            "viewport": settings.viewport,
            "no_viewport": False,
            "accept_downloads": True,
            "ignore_https_errors": True,
        }
        if record_video:
            context_kwargs["record_video_dir"] = video_dir
            context_kwargs["record_video_size"] = settings.viewport

        context = browser.new_context(**context_kwargs)
        
        # Start tracing if configured
        if settings.trace in ("on", "retain-on-failure"):
            context.tracing.start(screenshots=True, snapshots=True, sources=True)

        return context

    @staticmethod
    def create_page(context: BrowserContext) -> Page:
        page = context.new_page()
        page.set_default_timeout(settings.timeout)
        page.set_default_navigation_timeout(settings.navigation_timeout)
        return page

