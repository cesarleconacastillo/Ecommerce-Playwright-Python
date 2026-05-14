import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser

        browser.close()

@pytest.fixture(scope="session")
def page(browser):

    context = browser.new_context()
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    page = context.new_page()

    yield page

    context.tracing.stop(
        path="reports/traces/trace.zip"
    )

    page.close()