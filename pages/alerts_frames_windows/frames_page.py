import allure
from core.base_page import BasePage


class FramesPage(BasePage):
    """Page Object for DemoQA Frames and Nested Frames pages."""

    FRAMES_URL = "/frames"
    NESTED_FRAMES_URL = "/nestedframes"

    @allure.step("Open Frames page")
    def open_frames(self):
        self.navigate(self.FRAMES_URL)
        return self

    @allure.step("Open Nested Frames page")
    def open_nested_frames(self):
        self.navigate(self.NESTED_FRAMES_URL)
        return self

    @allure.step("Get text from Frame 1")
    def get_frame1_heading(self) -> str:
        frame = self.page.frame_locator("#frame1")
        return frame.locator("#sampleHeading").inner_text().strip()

    @allure.step("Get text from parent iframe in Nested Frames")
    def get_parent_frame_text(self) -> str:
        parent_frame = self.page.frame_locator("#frame1")
        return parent_frame.locator("body").inner_text().strip()

    @allure.step("Get text from nested child iframe")
    def get_child_frame_text(self) -> str:
        parent_frame = self.page.frame_locator("#frame1")
        child_frame = parent_frame.frame_locator("iframe")
        return child_frame.locator("body").inner_text().strip()

