from typing import List
import allure
from core.base_page import BasePage


class SelectMenuPage(BasePage):
    """Page Object for DemoQA Select Menu page."""

    URL = "/select-menu"

    # Locators
    SELECT_VALUE = "#withOptGroup"
    SELECT_VALUE_INPUT = "#react-select-2-input"
    SELECT_ONE = "#selectOne"
    SELECT_ONE_INPUT = "#react-select-3-input"
    OLD_STYLE_SELECT = "#oldSelectMenu"
    MULTI_SELECT_INPUT = "#react-select-4-input"
    STANDARD_MULTI_SELECT = "#cars"

    @allure.step("Open Select Menu page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Select React Option: {value}")
    def select_react_value(self, value: str):
        self.click(self.SELECT_VALUE)
        self.fill(self.SELECT_VALUE_INPUT, value)
        self.page.keyboard.press("Enter")
        return self

    @allure.step("Select Old Style dropdown option by label: {label}")
    def select_old_style(self, label: str):
        self.select_option(self.OLD_STYLE_SELECT, label=label)
        return self

    @allure.step("Get selected Old Style option value")
    def get_old_style_value(self) -> str:
        return self.page.locator(self.OLD_STYLE_SELECT).input_value()

    @allure.step("Select multiple cars from standard multi select: {car_values}")
    def select_standard_multi(self, car_values: List[str]):
        # Playwright select_option accepts 'value' as a string or list of strings
        self.page.locator(self.STANDARD_MULTI_SELECT).select_option(value=car_values)
        return self
