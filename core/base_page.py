from typing import Optional, List
import allure
from playwright.sync_api import Page, Locator
from config.config import settings
from core.logger import logger


class BasePage:
    """Base class for all Page Objects in the framework, encapsulating Playwright interactions."""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to {url_or_path}")
    def navigate(self, url_or_path: str = ""):
        if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
            target_url = url_or_path
        else:
            base = settings.base_url.rstrip("/")
            path = url_or_path.lstrip("/")
            target_url = f"{base}/{path}" if path else base

        logger.info(f"Navigating to: {target_url}")
        self.page.goto(target_url, wait_until="domcontentloaded")
        self.remove_ads_and_banners()

    @allure.step("Remove obstruction ads and banners")
    def remove_ads_and_banners(self):
        """Removes floating ads and fixed footer banners commonly obstructing DemoQA pages."""
        try:
            self.page.evaluate(
                """() => {
                    const selectors = [
                        '#fixedban',
                        'footer',
                        'iframe[id^="google_ads"]',
                        '#adplus-anchor',
                        '.GoogleActiveViewClass'
                    ];
                    selectors.forEach(sel => {
                        document.querySelectorAll(sel).forEach(el => el.remove());
                    });
                }"""
            )
        except Exception as e:
            logger.debug(f"Non-critical issue while removing banners/ads: {e}")

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    @allure.step("Click element: {selector}")
    def click(self, selector: str, timeout: Optional[int] = None, force: bool = False):
        logger.info(f"Clicking element: {selector}")
        self.remove_ads_and_banners()
        loc = self.page.locator(selector).first
        loc.scroll_into_view_if_needed(timeout=timeout or settings.timeout)
        loc.click(timeout=timeout or settings.timeout, force=force)

    @allure.step("Double click element: {selector}")
    def double_click(self, selector: str, timeout: Optional[int] = None):
        logger.info(f"Double-clicking element: {selector}")
        self.remove_ads_and_banners()
        loc = self.page.locator(selector).first
        loc.scroll_into_view_if_needed(timeout=timeout or settings.timeout)
        loc.dblclick(timeout=timeout or settings.timeout)

    @allure.step("Right click element: {selector}")
    def right_click(self, selector: str, timeout: Optional[int] = None):
        logger.info(f"Right-clicking element: {selector}")
        self.remove_ads_and_banners()
        loc = self.page.locator(selector).first
        loc.scroll_into_view_if_needed(timeout=timeout or settings.timeout)
        loc.click(button="right", timeout=timeout or settings.timeout)

    @allure.step("Fill input: {selector} with text '{text}'")
    def fill(self, selector: str, text: str, timeout: Optional[int] = None):
        logger.info(f"Filling '{selector}' with: {text}")
        self.remove_ads_and_banners()
        loc = self.page.locator(selector).first
        loc.scroll_into_view_if_needed(timeout=timeout or settings.timeout)
        loc.fill(text, timeout=timeout or settings.timeout)

    @allure.step("Get text from element: {selector}")
    def get_text(self, selector: str, timeout: Optional[int] = None) -> str:
        loc = self.page.locator(selector).first
        text = loc.inner_text(timeout=timeout or settings.timeout)
        logger.info(f"Read text from '{selector}': {text}")
        return text.strip()

    @allure.step("Get input value from: {selector}")
    def get_input_value(self, selector: str, timeout: Optional[int] = None) -> str:
        loc = self.page.locator(selector).first
        val = loc.input_value(timeout=timeout or settings.timeout)
        logger.info(f"Read input value from '{selector}': {val}")
        return val

    @allure.step("Check visibility of element: {selector}")
    def is_visible(self, selector: str, timeout: Optional[int] = None) -> bool:
        try:
            return self.page.locator(selector).first.is_visible(timeout=timeout or 5000)
        except Exception:
            return False

    @allure.step("Check if element is enabled: {selector}")
    def is_enabled(self, selector: str, timeout: Optional[int] = None) -> bool:
        try:
            return self.page.locator(selector).first.is_enabled(timeout=timeout or 5000)
        except Exception:
            return False

    @allure.step("Check if element is checked: {selector}")
    def is_checked(self, selector: str, timeout: Optional[int] = None) -> bool:
        return self.page.locator(selector).first.is_checked(timeout=timeout or settings.timeout)

    @allure.step("Select checkbox / radio: {selector}")
    def check(self, selector: str, timeout: Optional[int] = None, force: bool = False):
        logger.info(f"Checking element: {selector}")
        self.remove_ads_and_banners()
        self.page.locator(selector).first.check(timeout=timeout or settings.timeout, force=force)

    @allure.step("Uncheck checkbox: {selector}")
    def uncheck(self, selector: str, timeout: Optional[int] = None, force: bool = False):
        logger.info(f"Unchecking element: {selector}")
        self.remove_ads_and_banners()
        self.page.locator(selector).first.uncheck(timeout=timeout or settings.timeout, force=force)

    @allure.step("Select option in dropdown: {selector}")
    def select_option(
        self,
        selector: str,
        value: Optional[str] = None,
        label: Optional[str] = None,
        index: Optional[int] = None,
    ) -> List[str]:
        logger.info(f"Selecting dropdown option for: {selector} (value={value}, label={label}, index={index})")
        loc = self.page.locator(selector).first
        if value is not None:
            return loc.select_option(value=value)
        elif label is not None:
            return loc.select_option(label=label)
        elif index is not None:
            return loc.select_option(index=index)
        return []

    @allure.step("Scroll element into view: {selector}")
    def scroll_into_view(self, selector: str):
        self.page.locator(selector).first.scroll_into_view_if_needed()

    @allure.step("Hover on element: {selector}")
    def hover(self, selector: str):
        logger.info(f"Hovering on: {selector}")
        self.page.locator(selector).first.hover()

    @allure.step("Drag '{source_selector}' and drop onto '{target_selector}'")
    def drag_and_drop(self, source_selector: str, target_selector: str):
        logger.info(f"Dragging {source_selector} to {target_selector}")
        self.remove_ads_and_banners()
        source = self.page.locator(source_selector).first
        target = self.page.locator(target_selector).first
        source.drag_to(target)

    @allure.step("Upload file '{file_path}' to {selector}")
    def upload_file(self, selector: str, file_path: str):
        logger.info(f"Uploading file {file_path} to {selector}")
        self.page.locator(selector).first.set_input_files(file_path)

    @allure.step("Wait for selector: {selector} (state={state})")
    def wait_for_selector(self, selector: str, state: str = "visible", timeout: Optional[int] = None):
        self.page.locator(selector).first.wait_for(state=state, timeout=timeout or settings.timeout)

    @allure.step("Take page screenshot: {name}")
    def take_screenshot(self, name: str = "screenshot") -> bytes:
        screenshot_bytes = self.page.screenshot(full_page=True)
        allure.attach(
            screenshot_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
        return screenshot_bytes

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

