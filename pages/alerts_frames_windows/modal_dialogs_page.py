import allure
from core.base_page import BasePage


class ModalDialogsPage(BasePage):
    """Page Object for DemoQA Modal Dialogs page."""

    URL = "/modal-dialogs"

    # Small Modal
    SMALL_MODAL_BUTTON = "#showSmallModal"
    SMALL_MODAL_TITLE = "#example-modal-sizes-title-sm"
    SMALL_MODAL_BODY = ".modal-body"
    CLOSE_SMALL_MODAL_BUTTON = "#closeSmallModal"

    # Large Modal
    LARGE_MODAL_BUTTON = "#showLargeModal"
    LARGE_MODAL_TITLE = "#example-modal-sizes-title-lg"
    LARGE_MODAL_BODY = ".modal-body"
    CLOSE_LARGE_MODAL_BUTTON = "#closeLargeModal"

    @allure.step("Open Modal Dialogs page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Open Small Modal")
    def open_small_modal(self):
        self.click(self.SMALL_MODAL_BUTTON)
        self.wait_for_selector(self.SMALL_MODAL_TITLE)
        return self

    @allure.step("Get Small Modal title and body text")
    def get_small_modal_content(self) -> dict:
        return {
            "title": self.get_text(self.SMALL_MODAL_TITLE),
            "body": self.get_text(self.SMALL_MODAL_BODY),
        }

    @allure.step("Close Small Modal")
    def close_small_modal(self):
        self.click(self.CLOSE_SMALL_MODAL_BUTTON)
        return self

    @allure.step("Open Large Modal")
    def open_large_modal(self):
        self.click(self.LARGE_MODAL_BUTTON)
        self.wait_for_selector(self.LARGE_MODAL_TITLE)
        return self

    @allure.step("Get Large Modal title and body text")
    def get_large_modal_content(self) -> dict:
        return {
            "title": self.get_text(self.LARGE_MODAL_TITLE),
            "body": self.get_text(self.LARGE_MODAL_BODY),
        }

    @allure.step("Close Large Modal")
    def close_large_modal(self):
        self.click(self.CLOSE_LARGE_MODAL_BUTTON)
        return self

