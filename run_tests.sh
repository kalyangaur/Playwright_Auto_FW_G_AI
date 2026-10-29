#!/usr/bin/env bash
set -e

echo "========================================================"
echo "Playwright Automation Framework - Test Runner"
echo "========================================================"

# Run Pytest with Allure report generation
pytest -v --alluredir=allure-results --clean-alluredir "$@"

# Generate and open Allure report if allure CLI is available
if command -v allure &> /dev/null; then
    echo "Serving Allure Report..."
    allure serve allure-results
else
    echo "Allure CLI not detected in PATH."
    echo "Results stored in 'allure-results' folder."
    echo "To view reports, install Allure CLI and run: allure serve allure-results"
fi

