import allure
from core.base_page import BasePage


class AccordianPage(BasePage):
    """Page Object for DemoQA Accordian page (supports modern Bootstrap accordion & legacy IDs)."""

    URL = "/accordian"

    # Headings
    SECTION_1_HEADING = ".accordion-item:nth-child(1) .accordion-button, #section1Heading"
    SECTION_2_HEADING = ".accordion-item:nth-child(2) .accordion-button, #section2Heading"
    SECTION_3_HEADING = ".accordion-item:nth-child(3) .accordion-button, #section3Heading"

    # Collapse containers
    SECTION_1_CONTENT = ".accordion-item:nth-child(1) .accordion-collapse, #section1Content"
    SECTION_2_CONTENT = ".accordion-item:nth-child(2) .accordion-collapse, #section2Content"
    SECTION_3_CONTENT = ".accordion-item:nth-child(3) .accordion-collapse, #section3Content"

    @allure.step("Open Accordian page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Toggle section 1")
    def toggle_section_1(self):
        self.click(self.SECTION_1_HEADING)
        self.page.wait_for_timeout(400)
        return self

    @allure.step("Toggle section 2")
    def toggle_section_2(self):
        self.click(self.SECTION_2_HEADING)
        self.page.wait_for_timeout(400)
        return self

    @allure.step("Toggle section 3")
    def toggle_section_3(self):
        self.click(self.SECTION_3_HEADING)
        self.page.wait_for_timeout(400)
        return self

    @allure.step("Check if section 1 is expanded")
    def is_section_1_expanded(self) -> bool:
        loc = self.page.locator(self.SECTION_1_CONTENT).first
        classes = loc.get_attribute("class") or ""
        return "show" in classes

    @allure.step("Check if section 2 is expanded")
    def is_section_2_expanded(self) -> bool:
        loc = self.page.locator(self.SECTION_2_CONTENT).first
        classes = loc.get_attribute("class") or ""
        return "show" in classes

    @allure.step("Check if section 3 is expanded")
    def is_section_3_expanded(self) -> bool:
        loc = self.page.locator(self.SECTION_3_CONTENT).first
        classes = loc.get_attribute("class") or ""
        return "show" in classes
