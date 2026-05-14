import os
import pytest

pytest_plugins = [
    "fixtures.browser",
    "fixtures.data"
]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = (
                f"reports/screenshots/{item.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )