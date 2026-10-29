import allure
from core.base_page import BasePage


class TabsPage(BasePage):
    """Page Object for DemoQA Tabs page."""

    URL = "/tabs"

    # Locators
    TAB_WHAT = "#demo-tab-what"
    TAB_ORIGIN = "#demo-tab-origin"
    TAB_USE = "#demo-tab-use"
    TAB_MORE = "#demo-tab-more"

    PANE_WHAT = "#demo-tabpane-what"
    PANE_ORIGIN = "#demo-tabpane-origin"
    PANE_USE = "#demo-tabpane-use"

    @allure.step("Open Tabs page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Switch to 'Origin' tab")
    def switch_to_origin(self):
        self.click(self.TAB_ORIGIN)
        return self

    @allure.step("Switch to 'Use' tab")
    def switch_to_use(self):
        self.click(self.TAB_USE)
        return self

    @allure.step("Switch to 'What' tab")
    def switch_to_what(self):
        self.click(self.TAB_WHAT)
        return self

    @allure.step("Get text from What tab pane")
    def get_what_pane_text(self) -> str:
        return self.get_text(self.PANE_WHAT) if self.is_visible(self.PANE_WHAT) else ""

    @allure.step("Get text from Origin tab pane")
    def get_origin_pane_text(self) -> str:
        return self.get_text(self.PANE_ORIGIN) if self.is_visible(self.PANE_ORIGIN) else ""

    @allure.step("Get text from Use tab pane")
    def get_use_pane_text(self) -> str:
        return self.get_text(self.PANE_USE) if self.is_visible(self.PANE_USE) else ""

    @allure.step("Check if More tab is disabled")
    def is_more_tab_disabled(self) -> bool:
        classes = self.page.locator(self.TAB_MORE).get_attribute("class") or ""
        return "disabled" in classes

