import pytest
import allure


@allure.epic("DemoQA Test Automation")
@allure.feature("Widgets Module")
class TestWidgets:
    """Test suite covering Widgets components (TC19 to TC25)."""

    @allure.story("Accordian Expand and Collapse")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC19 - Verify expanding and collapsing accordian cards")
    @pytest.mark.widgets
    @pytest.mark.regression
    def test_accordian_sections(self, accordian_page):
        accordian_page.open()
        
        # Section 1 is expanded by default
        assert accordian_page.is_section_1_expanded()

        # Expand Section 2 (Section 1 should collapse)
        accordian_page.toggle_section_2()
        assert accordian_page.is_section_2_expanded()
        assert not accordian_page.is_section_1_expanded()

    @allure.story("Auto Complete Multi & Single Inputs")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC20 - Verify auto-complete multi-color and single-color selection")
    @pytest.mark.widgets
    @pytest.mark.regression
    def test_auto_complete_multi_and_single(self, auto_complete_page):
        auto_complete_page.open()
        
        # Multi Input
        colors = ["Red", "Green"]
        auto_complete_page.add_multiple_colors(colors)
        multi_selected = auto_complete_page.get_multi_color_values()
        for color in colors:
            assert color in multi_selected

        # Single Input
        auto_complete_page.set_single_color("Blue")
        assert auto_complete_page.get_single_color_value() == "Blue"

    @allure.story("Date Picker Selection")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC21 - Verify selecting date from Date Picker calendar widget")
    @pytest.mark.widgets
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_date_picker_selection(self, date_picker_page):
        date_picker_page.open()
        date_picker_page.select_date(month="June", year="2025", day="18")

        selected = date_picker_page.get_selected_date()
        # DemoQA format is MM/DD/YYYY
        assert "06/18/2025" in selected

    @allure.story("Slider Interaction")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC22 - Verify moving slider updates synced value badge")
    @pytest.mark.widgets
    @pytest.mark.regression
    def test_slider_movement(self, slider_page):
        slider_page.open()
        target_val = 68
        slider_page.set_slider_value(target_val)

        val_badge = slider_page.get_slider_value()
        assert val_badge == str(target_val)

    @allure.story("Progress Bar Controls")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC23 - Verify progress bar completion and reset")
    @pytest.mark.widgets
    @pytest.mark.regression
    def test_progress_bar(self, progress_bar_page):
        progress_bar_page.open()
        progress_bar_page.toggle_progress()
        
        # Wait until full completion
        progress_bar_page.wait_until_complete()
        assert progress_bar_page.get_progress_value() == 100

        # Reset
        progress_bar_page.reset()
        assert progress_bar_page.get_progress_value() == 0

    @allure.story("Tabs Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC24 - Verify switching tabs and disabled tab status")
    @pytest.mark.widgets
    @pytest.mark.regression
    def test_tabs_navigation(self, tabs_page):
        tabs_page.open()

        # Check default tab
        assert len(tabs_page.get_what_pane_text()) > 20

        # Switch to Origin
        tabs_page.switch_to_origin()
        assert len(tabs_page.get_origin_pane_text()) > 20

        # Switch to Use
        tabs_page.switch_to_use()
        assert len(tabs_page.get_use_pane_text()) > 20

        # Check More tab is disabled
        assert tabs_page.is_more_tab_disabled()

    @allure.story("Select Menu Dropdowns")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC25 - Verify React select and native HTML select dropdowns")
    @pytest.mark.widgets
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_select_menu_dropdowns(self, select_menu_page):
        select_menu_page.open()

        # React Dropdown
        select_menu_page.select_react_value("Group 1, option 2")

        # Native Old Style Select
        select_menu_page.select_old_style("Purple")
        assert select_menu_page.get_old_style_value() == "4"  # Value 4 corresponds to Purple

        # Standard Multi Select
        select_menu_page.select_standard_multi(["volvo", "audi"])

