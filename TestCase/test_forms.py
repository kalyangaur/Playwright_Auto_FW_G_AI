from pathlib import Path
import pytest
import allure
from utils.helpers import DataGenerator
from test_data import load_test_data


@allure.epic("DemoQA Test Automation")
@allure.feature("Forms Module")
class TestForms:
    """Test suite covering Practice Forms (TC11 to TC12)."""

    @allure.story("Student Registration Form Full Submission")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("TC11 - Verify submission of entire registration practice form")
    @pytest.mark.forms
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_practice_form_all_fields(self, practice_form_page):
        data = load_test_data()["practice_form"]
        unique_email = DataGenerator.random_email()
        sample_file = Path("test_data/sample_upload.txt").resolve()

        practice_form_page.open()
        practice_form_page.fill_personal_info(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=unique_email,
            gender=data["gender"],
            mobile=data["mobile"],
        )
        practice_form_page.add_subjects(data["subjects"])
        practice_form_page.select_hobbies(data["hobbies"])
        practice_form_page.upload_photo(str(sample_file))
        practice_form_page.fill_address(
            address=data["current_address"],
            state=data["state"],
            city=data["city"],
        )
        practice_form_page.submit()

        assert practice_form_page.is_submission_modal_visible(), "Submission modal dialog was not displayed"
        assert "Thanks for submitting the form" in practice_form_page.get_modal_title()

        submission_data = practice_form_page.get_submission_data()
        assert f"{data['first_name']} {data['last_name']}" in submission_data.get("Student Name", "")
        assert unique_email in submission_data.get("Student Email", "")
        assert data["gender"] in submission_data.get("Gender", "")
        assert data["mobile"] in submission_data.get("Mobile", "")

        practice_form_page.close_modal()

    @allure.story("Student Registration Form Mandatory Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC12 - Verify form submission validation with empty required fields")
    @pytest.mark.forms
    @pytest.mark.regression
    def test_practice_form_validation(self, practice_form_page):
        practice_form_page.open()
        practice_form_page.submit()

        # Modal should not show up for invalid submission
        assert not practice_form_page.is_submission_modal_visible(), "Modal should not be displayed when empty"
        
        # Verify HTML5 pseudo-class :invalid is applied to mandatory inputs
        first_name_valid = practice_form_page.page.evaluate(
            "document.querySelector('#firstName').checkValidity()"
        )
        assert not first_name_valid, "First name should be invalid on empty submit"

