import allure
from core.base_page import BasePage


class AlertsPage(BasePage):
    """Page Object for DemoQA Alerts page."""

    URL = "/alerts"

    # Locators
    ALERT_BUTTON = "#alertButton"
    TIMER_ALERT_BUTTON = "#timerAlertButton"
    CONFIRM_BUTTON = "#confirmButton"
    PROMPT_BUTTON = "#promtButton"

    CONFIRM_RESULT = "#confirmResult"
    PROMPT_RESULT = "#promptResult"

    @allure.step("Open Alerts page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Trigger simple alert and accept")
    def trigger_simple_alert(self) -> str:
        alert_text = []

        def handle_dialog(dialog):
            alert_text.append(dialog.message)
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.click(self.ALERT_BUTTON)
        return alert_text[0] if alert_text else ""

    @allure.step("Trigger confirm box (accept={accept})")
    def trigger_confirm_box(self, accept: bool = True) -> str:
        confirm_text = []

        def handle_dialog(dialog):
            confirm_text.append(dialog.message)
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", handle_dialog)
        self.click(self.CONFIRM_BUTTON)
        return confirm_text[0] if confirm_text else ""

    @allure.step("Get confirm result text")
    def get_confirm_result(self) -> str:
        return self.get_text(self.CONFIRM_RESULT) if self.is_visible(self.CONFIRM_RESULT) else ""

    @allure.step("Trigger prompt box and enter '{text}'")
    def trigger_prompt_box(self, text: str):
        def handle_dialog(dialog):
            dialog.accept(text)

        self.page.once("dialog", handle_dialog)
        self.click(self.PROMPT_BUTTON)
        return self

    @allure.step("Get prompt result text")
    def get_prompt_result(self) -> str:
        return self.get_text(self.PROMPT_RESULT) if self.is_visible(self.PROMPT_RESULT) else ""

