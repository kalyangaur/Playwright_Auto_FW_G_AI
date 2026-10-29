import allure
from core.base_page import BasePage


class LinksPage(BasePage):
    """Page Object for DemoQA Links page."""

    URL = "/links"

    # Locators
    SIMPLE_LINK = "#simpleLink"
    DYNAMIC_LINK = "#dynamicLink"
    CREATED_LINK = "#created"
    NO_CONTENT_LINK = "#no-content"
    BAD_REQUEST_LINK = "#bad-request"
    LINK_RESPONSE = "#linkResponse"

    @allure.step("Open Links page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Click simple link and wait for new page tab")
    def click_simple_link_new_page(self):
        with self.page.context.expect_page() as new_page_info:
            self.click(self.SIMPLE_LINK)
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

    @allure.step("Click API link: {selector}")
    def click_api_link(self, link_name: str = "created"):
        mapping = {
            "created": self.CREATED_LINK,
            "no-content": self.NO_CONTENT_LINK,
            "bad-request": self.BAD_REQUEST_LINK,
        }
        target = mapping.get(link_name, self.CREATED_LINK)
        self.click(target)
        return self

    @allure.step("Get link API response text")
    def get_link_response(self) -> str:
        self.wait_for_selector(self.LINK_RESPONSE)
        return self.get_text(self.LINK_RESPONSE)

