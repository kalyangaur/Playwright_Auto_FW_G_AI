import allure
from core.base_page import BasePage


class BrowserWindowsPage(BasePage):
    """Page Object for DemoQA Browser Windows page."""

    URL = "/browser-windows"

    # Locators
    TAB_BUTTON = "#tabButton"
    WINDOW_BUTTON = "#windowButton"
    MESSAGE_WINDOW_BUTTON = "#messageWindowButton"

    @allure.step("Open Browser Windows page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Click 'New Tab' button and switch to new page")
    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.click(self.TAB_BUTTON)
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

    @allure.step("Click 'New Window' button and switch to new page")
    def open_new_window(self):
        with self.page.context.expect_page() as new_page_info:
            self.click(self.WINDOW_BUTTON)
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

