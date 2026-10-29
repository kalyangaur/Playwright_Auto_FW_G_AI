import allure
from core.base_page import BasePage


class BrokenLinksImagesPage(BasePage):
    """Page Object for DemoQA Broken Links & Images page."""

    URL = "/broken"

    # Valid image is the ToolsQA brand image, broken image is the corrupted sample image
    VALID_IMAGE = "header img, img[src*='Toolsqa']"
    BROKEN_IMAGE = "img[src*='Toolsqa_1.jpg'], img[src*='Toolsqa_1']"
    VALID_LINK = "xpath=//a[contains(text(), 'Valid Link')]"
    BROKEN_LINK = "xpath=//a[contains(text(), 'Broken Link')]"

    @allure.step("Open Broken Links & Images page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Check natural width of image: {selector}")
    def get_image_natural_width(self, selector: str) -> int:
        loc = self.page.locator(selector).first
        loc.wait_for(state="attached", timeout=5000)
        return loc.evaluate("img => img.naturalWidth")

    @allure.step("Click valid link and verify navigation")
    def click_valid_link(self):
        self.click(self.VALID_LINK)
        return self

    @allure.step("Click broken link")
    def click_broken_link(self):
        self.click(self.BROKEN_LINK)
        return self
