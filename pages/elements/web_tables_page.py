from typing import List, Dict
import allure
from core.base_page import BasePage


class WebTablesPage(BasePage):
    """Page Object for DemoQA Web Tables page (supports modern Bootstrap table and ReactTable)."""

    URL = "/webtables"

    # Locators
    ADD_BUTTON = "#addNewRecordButton"
    SEARCH_INPUT = "#searchBox"

    # Registration Modal Locators
    FIRST_NAME_INPUT = "#firstName"
    LAST_NAME_INPUT = "#lastName"
    EMAIL_INPUT = "#userEmail"
    AGE_INPUT = "#age"
    SALARY_INPUT = "#salary"
    DEPARTMENT_INPUT = "#department"
    SUBMIT_BUTTON = "#submit"

    @allure.step("Open Web Tables page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Add new user record")
    def add_record(self, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
        self.click(self.ADD_BUTTON)
        self.wait_for_selector(self.FIRST_NAME_INPUT)
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.AGE_INPUT, age)
        self.fill(self.SALARY_INPUT, salary)
        self.fill(self.DEPARTMENT_INPUT, department)
        self.click(self.SUBMIT_BUTTON)
        self.page.wait_for_timeout(300)
        return self

    @allure.step("Search table by query: {query}")
    def search(self, query: str):
        self.fill(self.SEARCH_INPUT, query)
        self.page.wait_for_timeout(300)
        return self

    @allure.step("Clear search filter")
    def clear_search(self):
        self.fill(self.SEARCH_INPUT, "")
        self.page.wait_for_timeout(300)
        return self

    @allure.step("Edit record by email: {email}")
    def edit_record_by_email(self, email: str, new_salary: str = None, new_department: str = None):
        # Bootstrap table selector
        edit_button_xpath = f"//tr[.//td[contains(text(), '{email}')]]//span[contains(@id, 'edit-record') or @title='Edit']"
        edit_loc = self.page.locator(edit_button_xpath)
        if edit_loc.count() == 0:
            # ReactTable fallback
            edit_button_xpath = f"//div[contains(@class, 'rt-tr-group') and .//div[contains(text(), '{email}')]]//span[@title='Edit']"
            edit_loc = self.page.locator(edit_button_xpath)

        edit_loc.first.click()
        self.wait_for_selector(self.FIRST_NAME_INPUT)
        if new_salary:
            self.fill(self.SALARY_INPUT, new_salary)
        if new_department:
            self.fill(self.DEPARTMENT_INPUT, new_department)
        self.click(self.SUBMIT_BUTTON)
        self.page.wait_for_timeout(300)
        return self

    @allure.step("Delete record by email: {email}")
    def delete_record_by_email(self, email: str):
        delete_button_xpath = f"//tr[.//td[contains(text(), '{email}')]]//span[contains(@id, 'delete-record') or @title='Delete']"
        delete_loc = self.page.locator(delete_button_xpath)
        if delete_loc.count() == 0:
            delete_button_xpath = f"//div[contains(@class, 'rt-tr-group') and .//div[contains(text(), '{email}')]]//span[@title='Delete']"
            delete_loc = self.page.locator(delete_button_xpath)

        delete_loc.first.click()
        self.page.wait_for_timeout(300)
        return self

    @allure.step("Get all non-empty table records")
    def get_table_records(self) -> List[Dict[str, str]]:
        records = []
        # Bootstrap table check
        table_rows = self.page.locator("table tbody tr").all()
        if table_rows:
            for row in table_rows:
                cells = [c.strip() for c in row.locator("td").all_inner_texts()]
                if len(cells) >= 6 and cells[0] and not cells[0].isspace():
                    records.append({
                        "first_name": cells[0],
                        "last_name": cells[1],
                        "age": cells[2],
                        "email": cells[3],
                        "salary": cells[4],
                        "department": cells[5],
                    })
            return records

        # ReactTable fallback
        rt_rows = self.page.locator(".rt-tbody .rt-tr-group").all()
        for row in rt_rows:
            cells = [c.strip() for c in row.locator(".rt-td").all_inner_texts()]
            if len(cells) >= 6 and cells[0] and not cells[0].isspace():
                records.append({
                    "first_name": cells[0],
                    "last_name": cells[1],
                    "age": cells[2],
                    "email": cells[3],
                    "salary": cells[4],
                    "department": cells[5],
                })
        return records
