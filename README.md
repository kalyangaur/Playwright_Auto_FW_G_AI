# Playwright Python Automation Framework

An enterprise-ready, scalable end-to-end Web Test Automation Framework built with **Python**, **Playwright**, **Pytest**, and **Allure Report**, adhering to the **Page Object Model (POM)** design pattern.

Target Application: [https://demoqa.com/](https://demoqa.com/)

---

## 🌟 Key Highlights

- **Page Object Model (POM)**: Pure separation of concerns — locators and interaction logic encapsulated in Page classes; tests remain clean and declarative.
- **Robust BasePage**: Automatic dismissal of DemoQA Google Ads/floating banners, smart explicit waiting, unified clicking/typing, and cross-browser handling.
- **Rich Allure Reporting**: Detailed `@allure.step` annotations, severity levels, features, epics, automatic full-page screenshot capture, and HTML DOM attachment on failure.
- **Comprehensive Test Suite (30 Test Cases)**: Exactly 30 end-to-end test cases housed in `TestCase/`, covering Elements, Forms, Alerts, Frames, Windows, Widgets, and Interactions.
- **Flexible Configuration**: JSON + Environment variable overrides for Base URL, Browser (Chromium/Firefox/WebKit), Headless/Headed mode, timeouts, slow-mo, and tracing.
- **CI/CD Ready**: Pre-configured GitHub Actions workflow in `.github/workflows/tests.yml`.

---

## 📁 Directory Structure

```text
Playwright Auto FW - G-AI/
├── .github/
│   └── workflows/
│       └── tests.yml                     # GitHub Actions CI workflow
├── config/
│   ├── __init__.py
│   ├── config.py                         # Settings loader with env var support
│   └── settings.json                     # Default test configuration
├── core/
│   ├── __init__.py
│   ├── base_page.py                      # Robust Playwright BasePage wrapper
│   ├── driver_factory.py                 # Multi-browser & context factory
│   └── logger.py                         # Formatted console and file logging
├── pages/
│   ├── __init__.py
│   ├── elements/                         # Elements Module Pages (TextBox, CheckBox, etc.)
│   ├── forms/                            # Forms Module Pages (PracticeForm)
│   ├── alerts_frames_windows/            # Alerts, Windows, Frames & Modals Pages
│   ├── widgets/                          # Widgets Module Pages (Accordian, Tabs, etc.)
│   └── interactions/                     # Interactions Module Pages (Droppable, etc.)
├── TestCase/                             # Test Suite Directory
│   ├── __init__.py
│   ├── conftest.py                       # Page fixture dependency injection
│   ├── test_elements.py                  # TC01 - TC10: Elements suite
│   ├── test_forms.py                     # TC11 - TC12: Forms suite
│   ├── test_alerts_frames.py             # TC13 - TC18: Alerts, Frames & Windows suite
│   ├── test_widgets.py                   # TC19 - TC25: Widgets suite
│   └── test_interactions.py              # TC26 - TC30: Interactions suite
├── test_data/
│   ├── __init__.py
│   ├── test_data.json                    # Static test data payloads
│   └── sample_upload.txt                 # Asset for file upload testing
├── utils/
│   ├── __init__.py
│   ├── allure_helper.py                  # Allure attachments helper
│   └── helpers.py                        # Dynamic test data generator
├── conftest.py                           # Root fixtures & failure screenshot hooks
├── pytest.ini                            # Pytest runner configuration
├── requirements.txt                      # Project dependencies
├── run_tests.bat                         # Windows execution script
├── run_tests.sh                          # Linux / macOS execution script
└── README.md                             # Documentation
```

---

## 📋 Catalog of 30 Test Cases in `TestCase/`

| # | Test ID | Module | Scenario / Functionality |
|---|---|---|---|
| 1 | `TC01` | Elements | `test_text_box_submission` - Fill and verify Text Box output |
| 2 | `TC02` | Elements | `test_check_box_selection` - Expand tree and check sub-item |
| 3 | `TC03` | Elements | `test_radio_button_selection` - Select Yes/Impressive, verify No disabled |
| 4 | `TC04` | Elements | `test_web_table_add_record` - Add new employee record |
| 5 | `TC05` | Elements | `test_web_table_search_record` - Search table by keyword |
| 6 | `TC06` | Elements | `test_web_table_edit_record` - Edit existing record salary & department |
| 7 | `TC07` | Elements | `test_web_table_delete_record` - Delete specific table record |
| 8 | `TC08` | Elements | `test_buttons_actions` - Double Click, Right Click, and Dynamic Click |
| 9 | `TC09` | Elements | `test_links_new_tab` - Simple link open in new tab |
| 10 | `TC10` | Elements | `test_upload_and_download` - File download and upload verification |
| 11 | `TC11` | Forms | `test_practice_form_all_fields` - Complete student registration form |
| 12 | `TC12` | Forms | `test_practice_form_validation` - Empty form validation constraints |
| 13 | `TC13` | Alerts & Frames | `test_browser_windows_new_tab` - Switch to new browser tab |
| 14 | `TC14` | Alerts & Frames | `test_browser_windows_new_window` - Switch to new browser window |
| 15 | `TC15` | Alerts & Frames | `test_alert_simple_and_confirm` - Accept/dismiss alert dialogs |
| 16 | `TC16` | Alerts & Frames | `test_alert_prompt` - Input text in prompt dialog and verify |
| 17 | `TC17` | Alerts & Frames | `test_nested_iframes` - Traverse parent to child iframe |
| 18 | `TC18` | Alerts & Frames | `test_modal_dialogs` - Small and Large modal dialog handling |
| 19 | `TC19` | Widgets | `test_accordian_sections` - Expand/collapse accordian cards |
| 20 | `TC20` | Widgets | `test_auto_complete_multi_and_single` - Multi-tag & single select |
| 21 | `TC21` | Widgets | `test_date_picker_selection` - Calendar date selection |
| 22 | `TC22` | Widgets | `test_slider_movement` - Slider drag / keyboard value adjustment |
| 23 | `TC23` | Widgets | `test_progress_bar` - Progress bar completion & reset |
| 24 | `TC24` | Widgets | `test_tabs_navigation` - Tab switching and disabled tab check |
| 25 | `TC25` | Widgets | `test_select_menu_dropdowns` - React select, native `<select>`, multi-select |
| 26 | `TC26` | Interactions | `test_droppable_simple` - Drag and drop box to target |
| 27 | `TC27` | Interactions | `test_sortable_list` - Reorder items in sortable list |
| 28 | `TC28` | Interactions | `test_selectable_items` - Multiple list item selection |
| 29 | `TC29` | Dynamic | `test_dynamic_properties` - Dynamic delay: enable, color change, visible |
| 30 | `TC30` | Edge Cases | `test_broken_images_and_links` - Natural width check on valid vs broken image |

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python**: 3.10 or higher
- **Node.js**: (Optional, only needed if using Allure CLI standalone)

### 2. Setup Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install chromium
# Or install all supported browsers:
playwright install
```

---

## 🧪 Test Execution

### Run All 30 Tests
```bash
pytest
```

### Run Tests by Module
```bash
# Elements module (10 tests)
pytest TestCase/test_elements.py

# Forms module (2 tests)
pytest TestCase/test_forms.py

# Alerts & Frames module (6 tests)
pytest TestCase/test_alerts_frames.py

# Widgets module (7 tests)
pytest TestCase/test_widgets.py

# Interactions module (5 tests)
pytest TestCase/test_interactions.py
```

### Run Tests by Marker
```bash
# Smoke tests
pytest -m smoke

# Specific module markers
pytest -m elements
pytest -m forms
pytest -m alerts_frames
pytest -m widgets
pytest -m interactions
```

### Run with Cross-Browser Options
```bash
# Chromium (default)
pytest --browser-type=chromium

# Firefox
pytest --browser-type=firefox

# WebKit (Safari engine)
pytest --browser-type=webkit
```

### Headed Mode Execution (Watch the browser run)
```bash
pytest --headed
```

### Parallel Execution (Accelerate with pytest-xdist)
```bash
pytest -n 4
```

---

## 📊 Generating Allure Reports

The framework outputs Allure test results into `allure-results/` on each run.

### Serve Report (Auto-starts local web server):
```bash
allure serve allure-results
```

### Generate Static Report:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## ⚙️ Configuration Settings

Settings can be customized in `config/settings.json` or overridden via environment variables:

| Setting | JSON Key | Environment Variable | Default |
|---|---|---|---|
| Base URL | `base_url` | `BASE_URL` | `https://demoqa.com` |
| Browser | `browser` | `BROWSER` | `chromium` |
| Headless Mode | `headless` | `HEADLESS` | `true` |
| Default Timeout | `timeout` | `TIMEOUT` | `30000` ms |
| Navigation Timeout | `navigation_timeout` | `NAVIGATION_TIMEOUT` | `45000` ms |
| Slow Motion | `slow_mo` | `SLOW_MO` | `0` ms |
| Video Recording | `video` | - | `retain-on-failure` |
| Tracing | `trace` | - | `retain-on-failure` |

