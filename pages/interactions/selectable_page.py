from typing import List
import allure
from core.base_page import BasePage


class SelectablePage(BasePage):
    """Page Object for DemoQA Selectable page."""

    URL = "/selectable"

    # Locators
    LIST_ITEMS = "#verticalListContainer li"
    ACTIVE_ITEMS = "#verticalListContainer li.active"

    @allure.step("Open Selectable page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Click item by text: {item_text}")
    def select_item_by_text(self, item_text: str):
        item_loc = f"//ul[@id='verticalListContainer']/li[text()='{item_text}']"
        self.click(item_loc)
        return self

    @allure.step("Get list of currently active (selected) items")
    def get_selected_items(self) -> List[str]:
        items = self.page.locator(self.ACTIVE_ITEMS).all_inner_texts()
        return [item.strip() for item in items]

