import os
from pathlib import Path
import allure
from core.base_page import BasePage


class UploadDownloadPage(BasePage):
    """Page Object for DemoQA Upload and Download page."""

    URL = "/upload-download"

    # Locators
    DOWNLOAD_BUTTON = "#downloadButton"
    UPLOAD_INPUT = "#uploadFile"
    UPLOADED_FILE_PATH = "#uploadedFilePath"

    @allure.step("Open Upload and Download page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Download sample file")
    def trigger_download(self, save_dir: str = "reports/downloads") -> str:
        os.makedirs(save_dir, exist_ok=True)
        with self.page.expect_download() as download_info:
            self.click(self.DOWNLOAD_BUTTON)
        download = download_info.value
        save_path = os.path.join(save_dir, download.suggested_filename)
        download.save_as(save_path)
        return save_path

    @allure.step("Upload file: {file_path}")
    def upload_sample_file(self, file_path: str):
        abs_path = str(Path(file_path).resolve())
        self.upload_file(self.UPLOAD_INPUT, abs_path)
        return self

    @allure.step("Get uploaded file label text")
    def get_uploaded_file_name(self) -> str:
        if self.is_visible(self.UPLOADED_FILE_PATH):
            return self.get_text(self.UPLOADED_FILE_PATH)
        return ""

