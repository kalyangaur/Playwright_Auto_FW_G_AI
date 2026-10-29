import allure
from core.base_page import BasePage


class DatePickerPage(BasePage):
    """Page Object for DemoQA Date Picker page."""

    URL = "/date-picker"

    # Locators
    DATE_INPUT = "#datePickerMonthYearInput"
    DATE_TIME_INPUT = "#dateAndTimePickerInput"
    MONTH_SELECT = ".react-datepicker__month-select"
    YEAR_SELECT = ".react-datepicker__year-select"

    @allure.step("Open Date Picker page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Select date: month={month}, year={year}, day={day}")
    def select_date(self, month: str, year: str, day: str):
        self.click(self.DATE_INPUT)
        self.wait_for_selector(self.MONTH_SELECT)
        self.select_option(self.MONTH_SELECT, label=month)
        self.select_option(self.YEAR_SELECT, value=year)
        
        # Click on day that is not outside month
        day_selector = f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month')) and text()='{day}']"
        self.click(day_selector)
        return self

    @allure.step("Get selected date input value")
    def get_selected_date(self) -> str:
        return self.get_input_value(self.DATE_INPUT)

