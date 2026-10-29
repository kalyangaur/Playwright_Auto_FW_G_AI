from typing import List
import allure
from core.base_page import BasePage


class AutoCompletePage(BasePage):
    """Page Object for DemoQA Auto Complete page."""

    URL = "/auto-complete"

    # Locators
    MULTI_INPUT = "#autoCompleteMultipleInput"
    SINGLE_INPUT = "#autoCompleteSingleInput"
    MULTI_VALUES = ".auto-complete__multi-value__label"
    SINGLE_VALUE = ".auto-complete__single-value"

    @allure.step("Open Auto Complete page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Add multiple colors: {colors}")
    def add_multiple_colors(self, colors: List[str]):
        for color in colors:
            self.fill(self.MULTI_INPUT, color)
            self.page.keyboard.press("Enter")
        return self

    @allure.step("Set single color: {color}")
    def set_single_color(self, color: str):
        self.fill(self.SINGLE_INPUT, color)
        self.page.keyboard.press("Enter")
        return self

    @allure.step("Get list of selected multiple colors")
    def get_multi_color_values(self) -> List[str]:
        items = self.page.locator(self.MULTI_VALUES).all_inner_texts()
        return [item.strip() for item in items]

    @allure.step("Get selected single color")
    def get_single_color_value(self) -> str:
        if self.is_visible(self.SINGLE_VALUE):
            return self.get_text(self.SINGLE_VALUE)
        return ""

