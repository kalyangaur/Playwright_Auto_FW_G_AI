import allure
from core.base_page import BasePage


class DroppablePage(BasePage):
    """Page Object for DemoQA Droppable page."""

    URL = "/droppable"

    # Strictly scoped to simple drop container
    DRAGGABLE_BOX = "#simpleDropContainer #draggable"
    DROPPABLE_TARGET = "#simpleDropContainer #droppable"
    DROPPED_TEXT = "#simpleDropContainer #droppable p"

    @allure.step("Open Droppable page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Drag simple box to drop target using mouse actions")
    def drag_and_drop_simple(self):
        self.remove_ads_and_banners()
        
        # Ensure jQuery UI draggable / droppable event listeners have initialized
        self.page.wait_for_selector(f"{self.DRAGGABLE_BOX}.ui-draggable", timeout=10000)
        self.page.wait_for_selector(f"{self.DROPPABLE_TARGET}.ui-droppable", timeout=10000)
        self.page.wait_for_timeout(500)

        drag = self.page.locator(self.DRAGGABLE_BOX).first
        drop = self.page.locator(self.DROPPABLE_TARGET).first

        box_drag = drag.bounding_box()
        box_drop = drop.bounding_box()

        if box_drag and box_drop:
            start_x = box_drag["x"] + box_drag["width"] / 2
            start_y = box_drag["y"] + box_drag["height"] / 2
            end_x = box_drop["x"] + box_drop["width"] / 2
            end_y = box_drop["y"] + box_drop["height"] / 2

            self.page.mouse.move(start_x, start_y)
            self.page.mouse.down()
            self.page.mouse.move(end_x, end_y, steps=25)
            self.page.mouse.up()
            self.page.wait_for_timeout(1000)
        else:
            drag.drag_to(drop, force=True)

        return self

    @allure.step("Get drop target text")
    def get_droppable_text(self) -> str:
        drop = self.page.locator(self.DROPPABLE_TARGET).first
        p = drop.locator("p").first
        if p.is_visible():
            return p.inner_text().strip()
        return drop.inner_text().strip()
