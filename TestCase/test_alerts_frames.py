import pytest
import allure


@allure.epic("DemoQA Test Automation")
@allure.feature("Alerts, Frame & Windows Module")
class TestAlertsFrames:
    """Test suite covering Windows, Alerts, Frames & Modals (TC13 to TC18)."""

    @allure.story("Browser Windows - New Tab")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC13 - Verify opening and switching to new browser tab")
    @pytest.mark.alerts_frames
    @pytest.mark.regression
    def test_browser_windows_new_tab(self, browser_windows_page):
        browser_windows_page.open()
        new_tab = browser_windows_page.open_new_tab()

        assert "/sample" in new_tab.url
        heading_text = new_tab.locator("#sampleHeading").inner_text()
        assert "This is a sample page" in heading_text

        new_tab.close()

    @allure.story("Browser Windows - New Window")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC14 - Verify opening and switching to new browser window")
    @pytest.mark.alerts_frames
    @pytest.mark.regression
    def test_browser_windows_new_window(self, browser_windows_page):
        browser_windows_page.open()
        new_win = browser_windows_page.open_new_window()

        assert "/sample" in new_win.url
        heading_text = new_win.locator("#sampleHeading").inner_text()
        assert "This is a sample page" in heading_text

        new_win.close()

    @allure.story("Alerts - Simple and Confirm Alerts")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC15 - Verify handling simple alert and confirm alert dialogs")
    @pytest.mark.alerts_frames
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_alert_simple_and_confirm(self, alerts_page):
        alerts_page.open()

        # Simple Alert
        msg = alerts_page.trigger_simple_alert()
        assert "You clicked a button" in msg

        # Confirm Alert - Accept
        alerts_page.trigger_confirm_box(accept=True)
        assert alerts_page.get_confirm_result() == "You selected Ok"

        # Confirm Alert - Dismiss
        alerts_page.trigger_confirm_box(accept=False)
        assert alerts_page.get_confirm_result() == "You selected Cancel"

    @allure.story("Alerts - Prompt Alert")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC16 - Verify entering text into prompt alert dialog")
    @pytest.mark.alerts_frames
    @pytest.mark.regression
    def test_alert_prompt(self, alerts_page):
        alerts_page.open()
        prompt_input = "Automation Hero"
        alerts_page.trigger_prompt_box(prompt_input)

        result = alerts_page.get_prompt_result()
        assert prompt_input in result, f"Expected {prompt_input} in {result}"

    @allure.story("Frames - Nested Iframes")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC17 - Verify nested iframe content traversal")
    @pytest.mark.alerts_frames
    @pytest.mark.regression
    def test_nested_iframes(self, frames_page):
        frames_page.open_nested_frames()
        
        parent_text = frames_page.get_parent_frame_text()
        assert "Parent frame" in parent_text

        child_text = frames_page.get_child_frame_text()
        assert "Child Iframe" in child_text

    @allure.story("Modal Dialogs")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC18 - Verify opening and closing small and large modals")
    @pytest.mark.alerts_frames
    @pytest.mark.regression
    def test_modal_dialogs(self, modal_dialogs_page):
        modal_dialogs_page.open()

        # Small Modal
        modal_dialogs_page.open_small_modal()
        sm_content = modal_dialogs_page.get_small_modal_content()
        assert "Small Modal" in sm_content["title"]
        assert "This is a small modal" in sm_content["body"]
        modal_dialogs_page.close_small_modal()

        # Large Modal
        modal_dialogs_page.open_large_modal()
        lg_content = modal_dialogs_page.get_large_modal_content()
        assert "Large Modal" in lg_content["title"]
        assert len(lg_content["body"]) > 50
        modal_dialogs_page.close_large_modal()

