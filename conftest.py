import pytest
import allure
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

from .pages.create_account import CreateAccount
from .pages.eco_friendly import EcoFriendly
from .pages.sale import Sale


@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser_instance = browser_type.launch(headless=True)
        yield request.param, browser_instance
        browser_instance.close()


@pytest.fixture
def page(browser):
    browser_name, browser_instance = browser
    page = browser_instance.new_page()
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get('page')
        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_name = f'{datetime.now().strftime('%Y%m%d_%H%M%S')}_{item.name}.png'
            screenshot_path = f"screenshots/{screenshot_name}"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

            allure.attach(
                open(screenshot_path, "rb").read(),
                f'screenshot - {screenshot_name}',
                allure.attachment_type.PNG
            )


@pytest.fixture()
def create_account(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale(page):
    return Sale(page)
