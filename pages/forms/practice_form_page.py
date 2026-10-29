from typing import List, Dict, Optional
from pathlib import Path
import allure
from core.base_page import BasePage


class PracticeFormPage(BasePage):
    """Page Object for DemoQA Student Registration Practice Form."""

    URL = "/automation-practice-form"

    # Locators
    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    EMAIL = "#userEmail"
    GENDER_MALE = "label[for='gender-radio-1']"
    GENDER_FEMALE = "label[for='gender-radio-2']"
    GENDER_OTHER = "label[for='gender-radio-3']"
    MOBILE = "#userNumber"
    DOB_INPUT = "#dateOfBirthInput"
    SUBJECTS_INPUT = "#subjectsInput"
    HOBBY_SPORTS = "label[for='hobbies-checkbox-1']"
    HOBBY_READING = "label[for='hobbies-checkbox-2']"
    HOBBY_MUSIC = "label[for='hobbies-checkbox-3']"
    UPLOAD_PICTURE = "#uploadPicture"
    CURRENT_ADDRESS = "#currentAddress"
    STATE_DROPDOWN = "#state"
    STATE_INPUT = "#react-select-3-input"
    CITY_DROPDOWN = "#city"
    CITY_INPUT = "#react-select-4-input"
    SUBMIT_BUTTON = "#submit"

    # Submission Modal Locators
    MODAL_DIALOG = ".modal-dialog"
    MODAL_TITLE = "#example-modal-sizes-title-lg"
    MODAL_ROWS = ".table-responsive table tbody tr"
    CLOSE_MODAL_BUTTON = "#closeLargeModal"

    @allure.step("Open Practice Form page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Fill personal info: {first_name} {last_name}, {email}, {gender}, {mobile}")
    def fill_personal_info(self, first_name: str, last_name: str, email: str, gender: str, mobile: str):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)

        gender_map = {
            "Male": self.GENDER_MALE,
            "Female": self.GENDER_FEMALE,
            "Other": self.GENDER_OTHER,
        }
        target_gender = gender_map.get(gender, self.GENDER_MALE)
        self.click(target_gender)

        self.fill(self.MOBILE, mobile)
        return self

    @allure.step("Add subjects: {subjects}")
    def add_subjects(self, subjects: List[str]):
        for subject in subjects:
            self.fill(self.SUBJECTS_INPUT, subject)
            self.page.keyboard.press("Enter")
        return self

    @allure.step("Select hobbies: {hobbies}")
    def select_hobbies(self, hobbies: List[str]):
        hobby_map = {
            "Sports": self.HOBBY_SPORTS,
            "Reading": self.HOBBY_READING,
            "Music": self.HOBBY_MUSIC,
        }
        for hobby in hobbies:
            if hobby in hobby_map:
                self.click(hobby_map[hobby])
        return self

    @allure.step("Upload picture: {file_path}")
    def upload_photo(self, file_path: str):
        abs_path = str(Path(file_path).resolve())
        self.upload_file(self.UPLOAD_PICTURE, abs_path)
        return self

    @allure.step("Fill address and state/city: {address}, {state}, {city}")
    def fill_address(self, address: str, state: str = "NCR", city: str = "Delhi"):
        self.fill(self.CURRENT_ADDRESS, address)
        self.scroll_into_view(self.STATE_DROPDOWN)
        
        # Interact with React select for State
        self.click(self.STATE_DROPDOWN)
        self.fill(self.STATE_INPUT, state)
        self.page.keyboard.press("Enter")

        # Interact with React select for City
        self.click(self.CITY_DROPDOWN)
        self.fill(self.CITY_INPUT, city)
        self.page.keyboard.press("Enter")
        return self

    @allure.step("Submit form")
    def submit(self):
        self.remove_ads_and_banners()
        self.click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Check if submission modal is displayed")
    def is_submission_modal_visible(self) -> bool:
        return self.is_visible(self.MODAL_DIALOG)

    @allure.step("Get submission modal title")
    def get_modal_title(self) -> str:
        return self.get_text(self.MODAL_TITLE) if self.is_visible(self.MODAL_TITLE) else ""

    @allure.step("Get submission summary table data")
    def get_submission_data(self) -> Dict[str, str]:
        summary = {}
        rows = self.page.locator(self.MODAL_ROWS).all()
        for row in rows:
            tds = row.locator("td").all_inner_texts()
            if len(tds) >= 2:
                summary[tds[0].strip()] = tds[1].strip()
        return summary

    @allure.step("Close modal dialog")
    def close_modal(self):
        self.remove_ads_and_banners()
        self.click(self.CLOSE_MODAL_BUTTON)
        return self

