import pytest
from playwright.sync_api import Page
from pages.elements import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonPage,
    WebTablesPage,
    ButtonsPage,
    LinksPage,
    UploadDownloadPage,
    DynamicPropertiesPage,
)
from pages.forms import PracticeFormPage
from pages.alerts_frames_windows import (
    BrowserWindowsPage,
    AlertsPage,
    FramesPage,
    ModalDialogsPage,
)
from pages.widgets import (
    AccordianPage,
    AutoCompletePage,
    DatePickerPage,
    SliderPage,
    ProgressBarPage,
    TabsPage,
    SelectMenuPage,
)
from pages.interactions import (
    DroppablePage,
    SortablePage,
    SelectablePage,
    BrokenLinksImagesPage,
)


@pytest.fixture
def text_box_page(page: Page) -> TextBoxPage:
    return TextBoxPage(page)


@pytest.fixture
def check_box_page(page: Page) -> CheckBoxPage:
    return CheckBoxPage(page)


@pytest.fixture
def radio_button_page(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)


@pytest.fixture
def web_tables_page(page: Page) -> WebTablesPage:
    return WebTablesPage(page)


@pytest.fixture
def buttons_page(page: Page) -> ButtonsPage:
    return ButtonsPage(page)


@pytest.fixture
def links_page(page: Page) -> LinksPage:
    return LinksPage(page)


@pytest.fixture
def upload_download_page(page: Page) -> UploadDownloadPage:
    return UploadDownloadPage(page)


@pytest.fixture
def dynamic_properties_page(page: Page) -> DynamicPropertiesPage:
    return DynamicPropertiesPage(page)


@pytest.fixture
def practice_form_page(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)


@pytest.fixture
def browser_windows_page(page: Page) -> BrowserWindowsPage:
    return BrowserWindowsPage(page)


@pytest.fixture
def alerts_page(page: Page) -> AlertsPage:
    return AlertsPage(page)


@pytest.fixture
def frames_page(page: Page) -> FramesPage:
    return FramesPage(page)


@pytest.fixture
def modal_dialogs_page(page: Page) -> ModalDialogsPage:
    return ModalDialogsPage(page)


@pytest.fixture
def accordian_page(page: Page) -> AccordianPage:
    return AccordianPage(page)


@pytest.fixture
def auto_complete_page(page: Page) -> AutoCompletePage:
    return AutoCompletePage(page)


@pytest.fixture
def date_picker_page(page: Page) -> DatePickerPage:
    return DatePickerPage(page)


@pytest.fixture
def slider_page(page: Page) -> SliderPage:
    return SliderPage(page)


@pytest.fixture
def progress_bar_page(page: Page) -> ProgressBarPage:
    return ProgressBarPage(page)


@pytest.fixture
def tabs_page(page: Page) -> TabsPage:
    return TabsPage(page)


@pytest.fixture
def select_menu_page(page: Page) -> SelectMenuPage:
    return SelectMenuPage(page)


@pytest.fixture
def droppable_page(page: Page) -> DroppablePage:
    return DroppablePage(page)


@pytest.fixture
def sortable_page(page: Page) -> SortablePage:
    return SortablePage(page)


@pytest.fixture
def selectable_page(page: Page) -> SelectablePage:
    return SelectablePage(page)


@pytest.fixture
def broken_links_images_page(page: Page) -> BrokenLinksImagesPage:
    return BrokenLinksImagesPage(page)

