from typing import List
import allure
from core.base_page import BasePage


class SortablePage(BasePage):
    """Page Object for DemoQA Sortable page."""

    URL = "/sortable"

    # Locators
    LIST_ITEMS = "#demo-tabpane-list .list-group-item"

    @allure.step("Open Sortable page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Get list items order")
    def get_list_items_text(self) -> List[str]:
        items = self.page.locator(self.LIST_ITEMS).all_inner_texts()
        return [item.strip() for item in items]

    @allure.step("Drag item from index {source_index} to index {target_index}")
    def reorder_list_item(self, source_index: int, target_index: int):
        self.remove_ads_and_banners()
        items = self.page.locator(self.LIST_ITEMS).all()
        if source_index < len(items) and target_index < len(items):
            box_src = items[source_index].bounding_box()
            box_tgt = items[target_index].bounding_box()

            if box_src and box_tgt:
                start_x = box_src["x"] + box_src["width"] / 2
                start_y = box_src["y"] + box_src["height"] / 2
                offset_y = 10 if target_index > source_index else -10
                end_x = box_tgt["x"] + box_tgt["width"] / 2
                end_y = box_tgt["y"] + box_tgt["height"] + offset_y

                self.page.mouse.move(start_x, start_y)
                self.page.mouse.down()
                self.page.mouse.move(end_x, end_y, steps=15)
                self.page.mouse.up()
                self.page.wait_for_timeout(300)
            else:
                items[source_index].drag_to(items[target_index], force=True)

        return self
