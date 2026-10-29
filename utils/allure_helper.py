import json
import allure
from typing import Any


class AllureHelper:
    """Utility class to attach context, logs, and files to Allure Reports."""

    @staticmethod
    def attach_text(text: str, name: str = "Log Note"):
        allure.attach(
            text,
            name=name,
            attachment_type=allure.attachment_type.TEXT,
        )

    @staticmethod
    def attach_json(data: Any, name: str = "JSON Payload"):
        allure.attach(
            json.dumps(data, indent=2),
            name=name,
            attachment_type=allure.attachment_type.JSON,
        )

    @staticmethod
    def attach_screenshot(screenshot_bytes: bytes, name: str = "Screenshot"):
        allure.attach(
            screenshot_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )

    @staticmethod
    def attach_html(html_content: str, name: str = "Page HTML Source"):
        allure.attach(
            html_content,
            name=name,
            attachment_type=allure.attachment_type.HTML,
        )

