@echo off
echo ========================================================
echo Playwright Automation Framework - Test Runner
echo ========================================================

REM Run Pytest with Allure report generation
pytest -v --alluredir=allure-results --clean-alluredir %*

REM Generate and open Allure report if allure CLI is available
where allure >nul 2>nul
if %errorlevel% equ 0 (
    echo.
    echo Serving Allure Report...
    allure serve allure-results
) else (
    echo.
    echo Allure CLI not detected in PATH.
    echo Results stored in 'allure-results' folder.
    echo To view reports, install Allure CLI and run: allure serve allure-results
)

