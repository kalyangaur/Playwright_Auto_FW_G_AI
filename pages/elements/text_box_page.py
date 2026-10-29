import allure
from core.base_page import BasePage


class TextBoxPage(BasePage):
    """Page Object for DemoQA Text Box page."""

    URL = "/text-box"

    # Locators
    FULL_NAME_INPUT = "#userName"
    EMAIL_INPUT = "#userEmail"
    CURRENT_ADDRESS_INPUT = "#currentAddress"
    PERMANENT_ADDRESS_INPUT = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    
    OUTPUT_NAME = "#output #name"
    OUTPUT_EMAIL = "#output #email"
    OUTPUT_CURRENT_ADDRESS = "#output #currentAddress"
    OUTPUT_PERMANENT_ADDRESS = "#output #permanentAddress"

    @allure.step("Open Text Box page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Fill and submit text box form")
    def submit_form(self, full_name: str, email: str, current_address: str, permanent_address: str):
        self.fill(self.FULL_NAME_INPUT, full_name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.CURRENT_ADDRESS_INPUT, current_address)
        self.fill(self.PERMANENT_ADDRESS_INPUT, permanent_address)
        self.click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Get submitted output values")
    def get_output_data(self) -> dict:
        return {
            "name": self.get_text(self.OUTPUT_NAME) if self.is_visible(self.OUTPUT_NAME) else "",
            "email": self.get_text(self.OUTPUT_EMAIL) if self.is_visible(self.OUTPUT_EMAIL) else "",
            "current_address": self.get_text(self.OUTPUT_CURRENT_ADDRESS) if self.is_visible(self.OUTPUT_CURRENT_ADDRESS) else "",
            "permanent_address": self.get_text(self.OUTPUT_PERMANENT_ADDRESS) if self.is_visible(self.OUTPUT_PERMANENT_ADDRESS) else "",
        }

