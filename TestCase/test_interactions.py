import pytest
import allure


@allure.epic("DemoQA Test Automation")
@allure.feature("Interactions & Dynamic Module")
class TestInteractions:
    """Test suite covering Interactions and Edge cases (TC26 to TC30)."""

    @allure.story("Drag and Drop")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC26 - Verify simple drag and drop target drop feedback")
    @pytest.mark.interactions
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_droppable_simple(self, droppable_page):
        droppable_page.open()
        droppable_page.drag_and_drop_simple()

        assert droppable_page.get_droppable_text() == "Dropped!"

    @allure.story("Sortable List Reordering")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC27 - Verify reordering items in a sortable list")
    @pytest.mark.interactions
    @pytest.mark.regression
    def test_sortable_list(self, sortable_page):
        sortable_page.open()
        initial_order = sortable_page.get_list_items_text()
        assert len(initial_order) >= 2

        # Drag first item to third position
        sortable_page.reorder_list_item(0, 2)
        new_order = sortable_page.get_list_items_text()

        assert initial_order != new_order, "Item order did not change after drag and drop"

    @allure.story("Selectable List Items")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC28 - Verify clicking items applies active selection state")
    @pytest.mark.interactions
    @pytest.mark.regression
    def test_selectable_items(self, selectable_page):
        selectable_page.open()
        selectable_page.select_item_by_text("Cras justo odio")
        selectable_page.select_item_by_text("Morbi leo risus")

        active_items = selectable_page.get_selected_items()
        assert "Cras justo odio" in active_items
        assert "Morbi leo risus" in active_items

    @allure.story("Dynamic Properties Timed Changes")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC29 - Verify dynamic button enablement, color change, and visibility")
    @pytest.mark.interactions
    @pytest.mark.regression
    def test_dynamic_properties(self, dynamic_properties_page):
        dynamic_properties_page.open()

        # Verify button becomes enabled
        is_enabled = dynamic_properties_page.wait_until_enabled(timeout_ms=8000)
        assert is_enabled, "Button did not become enabled within timeout"

        # Verify button becomes visible
        is_visible = dynamic_properties_page.wait_until_visible(timeout_ms=8000)
        assert is_visible, "Button did not become visible within timeout"

        # Verify color changed
        assert dynamic_properties_page.has_color_changed(), "Color change class not present"

    @allure.story("Broken Images and Links")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC30 - Verify valid vs broken image rendering and links")
    @pytest.mark.interactions
    @pytest.mark.regression
    def test_broken_images_and_links(self, broken_links_images_page):
        broken_links_images_page.open()

        # Valid image should have naturalWidth > 0
        valid_width = broken_links_images_page.get_image_natural_width(broken_links_images_page.VALID_IMAGE)
        assert valid_width > 0, f"Expected valid image naturalWidth > 0, got {valid_width}"

        # Broken image should have naturalWidth == 0
        broken_width = broken_links_images_page.get_image_natural_width(broken_links_images_page.BROKEN_IMAGE)
        assert broken_width == 0, f"Expected broken image naturalWidth == 0, got {broken_width}"

