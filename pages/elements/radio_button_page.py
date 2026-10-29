import allure
from core.base_page import BasePage


class RadioButtonPage(BasePage):
    """Page Object for DemoQA Radio Button page."""

    URL = "/radio-button"

    # Locators (DemoQA uses custom styling where input is hidden and label is clicked)
    YES_LABEL = "label[for='yesRadio']"
    IMPRESSIVE_LABEL = "label[for='impressiveRadio']"
    NO_RADIO_INPUT = "#noRadio"
    NO_LABEL = "label[for='noRadio']"
    SUCCESS_TEXT = "p.mt-3 span.text-success"

    @allure.step("Open Radio Button page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Select 'Yes' radio option")
    def select_yes(self):
        self.click(self.YES_LABEL)
        return self

    @allure.step("Select 'Impressive' radio option")
    def select_impressive(self):
        self.click(self.IMPRESSIVE_LABEL)
        return self

    @allure.step("Get selected message text")
    def get_selected_text(self) -> str:
        if self.is_visible(self.SUCCESS_TEXT):
            return self.get_text(self.SUCCESS_TEXT)
        return ""

    @allure.step("Check if 'No' radio option is disabled")
    def is_no_radio_disabled(self) -> bool:
        return not self.is_enabled(self.NO_RADIO_INPUT)

