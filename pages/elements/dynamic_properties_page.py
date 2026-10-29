import allure
from core.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    """Page Object for DemoQA Dynamic Properties page."""

    URL = "/dynamic-properties"

    # Locators
    ENABLE_AFTER_BUTTON = "#enableAfter"
    COLOR_CHANGE_BUTTON = "#colorChange"
    VISIBLE_AFTER_BUTTON = "#visibleAfter"

    @allure.step("Open Dynamic Properties page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Wait for enable-after button to become enabled")
    def wait_until_enabled(self, timeout_ms: int = 10000) -> bool:
        loc = self.page.locator(self.ENABLE_AFTER_BUTTON)
        loc.wait_for(state="attached", timeout=timeout_ms)
        # Wait until it is enabled
        self.page.wait_for_function(
            "btn => !btn.disabled",
            arg=loc.element_handle(),
            timeout=timeout_ms,
        )
        return self.is_enabled(self.ENABLE_AFTER_BUTTON)

    @allure.step("Check if color change button has text-danger class")
    def has_color_changed(self) -> bool:
        classes = self.page.locator(self.COLOR_CHANGE_BUTTON).get_attribute("class") or ""
        return "text-danger" in classes

    @allure.step("Wait for visible-after button to become visible")
    def wait_until_visible(self, timeout_ms: int = 10000) -> bool:
        self.wait_for_selector(self.VISIBLE_AFTER_BUTTON, state="visible", timeout=timeout_ms)
        return self.is_visible(self.VISIBLE_AFTER_BUTTON)

