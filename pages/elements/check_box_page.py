from typing import List
import allure
from core.base_page import BasePage


class CheckBoxPage(BasePage):
    """Page Object for DemoQA Check Box page (compatible with both rc-tree and legacy rct tree)."""

    URL = "/checkbox"

    RESULT_CONTAINER = "#result"
    RESULT_ITEMS = "#result .text-success"

    @allure.step("Open Check Box page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Expand all directory nodes")
    def expand_all(self):
        # Check if legacy top expand all button exists
        expand_all_btn = self.page.locator("button[title='Expand all'], .rct-option-expand-all")
        if expand_all_btn.count() > 0 and expand_all_btn.first.is_visible():
            expand_all_btn.first.click()
            return self

        # Otherwise expand modern rc-tree switcher nodes
        max_depth = 5
        for _ in range(max_depth):
            switchers = self.page.locator(".rc-tree-switcher_close, .rct-collapse-btn").all()
            if not switchers:
                break
            for sw in switchers:
                try:
                    if sw.is_visible():
                        sw.click()
                        self.page.wait_for_timeout(200)
                except Exception:
                    pass
        return self

    @allure.step("Check item by title: {title}")
    def check_node(self, title: str):
        # Modern rc-tree
        rc_checkbox = self.page.locator(f"//span[@title='{title}']/preceding-sibling::span[contains(@class, 'rc-tree-checkbox')]")
        if rc_checkbox.count() > 0:
            rc_checkbox.first.click()
            return self

        # Legacy rct-tree
        rct_checkbox = self.page.locator(f"//span[contains(@class, 'rct-title') and text()='{title}']/preceding-sibling::span[@class='rct-checkbox']")
        if rct_checkbox.count() > 0:
            rct_checkbox.first.click()
            return self

        # Fallback to direct label or text click
        self.click(f"text={title}")
        return self

    @allure.step("Get list of selected results")
    def get_selected_results(self) -> List[str]:
        if not self.is_visible(self.RESULT_CONTAINER):
            return []
        items = self.page.locator(self.RESULT_ITEMS).all_inner_texts()
        if not items:
            # Fallback to splitting inner text of #result
            raw_text = self.get_text(self.RESULT_CONTAINER)
            items = raw_text.replace("You have selected :", "").split()
        return [item.strip().lower() for item in items if item.strip()]
