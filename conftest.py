from playwright.sync_api import Playwright

import time
import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, args=["--start-maximized"])
    # create a new incognito browser context.
    context = browser.new_context(no_viewport=True)
    # create a new page in a pristine context.
    page = context.new_page()
    page.goto("https://rozetka.com.ua")

    yield page
    page.close()
