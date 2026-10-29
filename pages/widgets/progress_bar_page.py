import allure
from core.base_page import BasePage


class ProgressBarPage(BasePage):
    """Page Object for DemoQA Progress Bar page."""

    URL = "/progress-bar"

    # Locators
    START_STOP_BUTTON = "#startStopButton"
    PROGRESS_BAR = ".progress-bar"
    RESET_BUTTON = "#resetButton"

    @allure.step("Open Progress Bar page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Click Start/Stop button")
    def toggle_progress(self):
        self.click(self.START_STOP_BUTTON)
        return self

    @allure.step("Get current progress percentage")
    def get_progress_value(self) -> int:
        val_str = self.page.locator(self.PROGRESS_BAR).get_attribute("aria-valuenow") or "0"
        return int(val_str)

    @allure.step("Wait until progress reaches 100%")
    def wait_until_complete(self, timeout_ms: int = 20000):
        self.page.wait_for_selector(
            f"{self.PROGRESS_BAR}[aria-valuenow='100']",
            timeout=timeout_ms,
        )
        return self

    @allure.step("Click Reset button")
    def reset(self):
        self.click(self.RESET_BUTTON)
        return self

