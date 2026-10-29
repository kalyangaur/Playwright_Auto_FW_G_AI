import allure
from core.base_page import BasePage


class ButtonsPage(BasePage):
    """Page Object for DemoQA Buttons page."""

    URL = "/buttons"

    # Locators
    DOUBLE_CLICK_BUTTON = "#doubleClickBtn"
    RIGHT_CLICK_BUTTON = "#rightClickBtn"
    DYNAMIC_CLICK_BUTTON = "//button[text()='Click Me']"

    DOUBLE_CLICK_MSG = "#doubleClickMessage"
    RIGHT_CLICK_MSG = "#rightClickMessage"
    DYNAMIC_CLICK_MSG = "#dynamicClickMessage"

    @allure.step("Open Buttons page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Perform double click action")
    def do_double_click(self):
        self.double_click(self.DOUBLE_CLICK_BUTTON)
        return self

    @allure.step("Perform right click action")
    def do_right_click(self):
        self.right_click(self.RIGHT_CLICK_BUTTON)
        return self

    @allure.step("Perform dynamic single click action")
    def do_dynamic_click(self):
        self.click(self.DYNAMIC_CLICK_BUTTON)
        return self

    @allure.step("Get double click confirmation message")
    def get_double_click_message(self) -> str:
        return self.get_text(self.DOUBLE_CLICK_MSG) if self.is_visible(self.DOUBLE_CLICK_MSG) else ""

    @allure.step("Get right click confirmation message")
    def get_right_click_message(self) -> str:
        return self.get_text(self.RIGHT_CLICK_MSG) if self.is_visible(self.RIGHT_CLICK_MSG) else ""

    @allure.step("Get dynamic single click confirmation message")
    def get_dynamic_click_message(self) -> str:
        return self.get_text(self.DYNAMIC_CLICK_MSG) if self.is_visible(self.DYNAMIC_CLICK_MSG) else ""

