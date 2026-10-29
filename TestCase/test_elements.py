import os
from pathlib import Path
import pytest
import allure
from utils.helpers import DataGenerator
from test_data import load_test_data


@allure.epic("DemoQA Test Automation")
@allure.feature("Elements Module")
class TestElements:
    """Test suite covering Elements components (TC01 to TC10)."""

    @allure.story("Text Box Form Submission")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC01 - Verify valid submission of Text Box form")
    @pytest.mark.elements
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_text_box_submission(self, text_box_page):
        data = load_test_data()["text_box"]
        text_box_page.open()
        text_box_page.submit_form(
            full_name=data["full_name"],
            email=data["email"],
            current_address=data["current_address"],
            permanent_address=data["permanent_address"],
        )
        output = text_box_page.get_output_data()

        assert data["full_name"] in output["name"], f"Expected {data['full_name']} in {output['name']}"
        assert data["email"] in output["email"], f"Expected {data['email']} in {output['email']}"
        assert data["current_address"] in output["current_address"]
        assert data["permanent_address"] in output["permanent_address"]

    @allure.story("Check Box Selection")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC02 - Verify expanding and selecting Check Box nodes")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_check_box_selection(self, check_box_page):
        check_box_page.open()
        check_box_page.expand_all()
        check_box_page.check_node("Notes")
        results = check_box_page.get_selected_results()

        assert "notes" in results, f"Expected 'notes' in selected results: {results}"

    @allure.story("Radio Button Selection")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC03 - Verify selecting Yes and Impressive radio buttons")
    @pytest.mark.elements
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_radio_button_selection(self, radio_button_page):
        radio_button_page.open()
        
        # Test Yes option
        radio_button_page.select_yes()
        assert radio_button_page.get_selected_text() == "Yes"

        # Test Impressive option
        radio_button_page.select_impressive()
        assert radio_button_page.get_selected_text() == "Impressive"

        # Verify No option is disabled
        assert radio_button_page.is_no_radio_disabled(), "Expected 'No' radio to be disabled"

    @allure.story("Web Tables - Add Record")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC04 - Verify adding a new record to Web Table")
    @pytest.mark.elements
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_web_table_add_record(self, web_tables_page):
        unique_email = DataGenerator.random_email()
        first_name = "Alan"
        last_name = "Turing"
        age = "41"
        salary = "120000"
        dept = "Cryptography"

        web_tables_page.open()
        web_tables_page.add_record(first_name, last_name, unique_email, age, salary, dept)

        records = web_tables_page.get_table_records()
        emails = [r["email"] for r in records]
        assert unique_email in emails, f"Record with {unique_email} was not found in table"

    @allure.story("Web Tables - Search Record")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC05 - Verify searching for a record in Web Table")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_web_table_search_record(self, web_tables_page):
        web_tables_page.open()
        web_tables_page.search("Cierra")
        records = web_tables_page.get_table_records()

        assert len(records) > 0, "No records found matching search"
        for r in records:
            assert "Cierra" in r["first_name"] or "Cierra" in r["last_name"]

    @allure.story("Web Tables - Edit Record")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC06 - Verify editing an existing record in Web Table")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_web_table_edit_record(self, web_tables_page):
        web_tables_page.open()
        target_email = "cierra@example.com"
        updated_salary = "75000"
        updated_dept = "Finance"

        web_tables_page.edit_record_by_email(target_email, new_salary=updated_salary, new_department=updated_dept)
        web_tables_page.search(target_email)
        records = web_tables_page.get_table_records()

        matching = [r for r in records if r["email"] == target_email]
        assert len(matching) == 1
        assert matching[0]["salary"] == updated_salary
        assert matching[0]["department"] == updated_dept

    @allure.story("Web Tables - Delete Record")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC07 - Verify deleting a record from Web Table")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_web_table_delete_record(self, web_tables_page):
        # Create a transient record then delete it
        temp_email = DataGenerator.random_email()
        web_tables_page.open()
        web_tables_page.add_record("Delete", "Me", temp_email, "30", "50000", "QA")
        
        # Verify it exists
        web_tables_page.search(temp_email)
        assert len(web_tables_page.get_table_records()) == 1

        # Delete record
        web_tables_page.delete_record_by_email(temp_email)
        web_tables_page.clear_search()
        web_tables_page.search(temp_email)

        # Verify it is removed
        assert len(web_tables_page.get_table_records()) == 0

    @allure.story("Buttons Actions")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC08 - Verify Double Click, Right Click, and Dynamic Click actions")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_buttons_actions(self, buttons_page):
        buttons_page.open()
        
        # Double Click
        buttons_page.do_double_click()
        assert buttons_page.get_double_click_message() == "You have done a double click"

        # Right Click
        buttons_page.do_right_click()
        assert buttons_page.get_right_click_message() == "You have done a right click"

        # Dynamic Single Click
        buttons_page.do_dynamic_click()
        assert buttons_page.get_dynamic_click_message() == "You have done a dynamic click"

    @allure.story("Links - New Tab Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC09 - Verify clicking link opens new page tab")
    @pytest.mark.elements
    @pytest.mark.regression
    def test_links_new_tab(self, links_page):
        links_page.open()
        new_page = links_page.click_simple_link_new_page()

        assert "demoqa.com" in new_page.url
        new_page.close()

    @allure.story("Upload and Download")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC10 - Verify file download and upload functionality")
    @pytest.mark.elements
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_upload_and_download(self, upload_download_page):
        upload_download_page.open()

        # Download Verification
        downloaded_file = upload_download_page.trigger_download()
        assert os.path.exists(downloaded_file), f"File {downloaded_file} was not downloaded"
        assert os.path.getsize(downloaded_file) > 0

        # Upload Verification
        sample_file = Path("test_data/sample_upload.txt").resolve()
        upload_download_page.upload_sample_file(str(sample_file))
        uploaded_name = upload_download_page.get_uploaded_file_name()
        assert "sample_upload.txt" in uploaded_name

