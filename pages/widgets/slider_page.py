import allure
from core.base_page import BasePage


class SliderPage(BasePage):
    """Page Object for DemoQA Slider page."""

    URL = "/slider"

    # Locators
    SLIDER_INPUT = "input.range-slider"
    SLIDER_VALUE = "#sliderValue"

    @allure.step("Open Slider page")
    def open(self):
        self.navigate(self.URL)
        return self

    @allure.step("Set slider value to: {target_value}")
    def set_slider_value(self, target_value: int):
        slider = self.page.locator(self.SLIDER_INPUT)
        slider.scroll_into_view_if_needed()
        
        # Programmatically set value and dispatch input/change events for robust React state sync
        self.page.evaluate(
            """({ sel, val }) => {
                const el = document.querySelector(sel);
                if (el) {
                    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(el, val);
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }""",
            {"sel": self.SLIDER_INPUT, "val": target_value},
        )
        return self

    @allure.step("Get slider display value")
    def get_slider_value(self) -> str:
        return self.get_input_value(self.SLIDER_VALUE)

