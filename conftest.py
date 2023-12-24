from playwright.sync_api import Playwright

import time
import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://rozetka.com.ua")
    page.set_default_timeout(5000)

    yield page
    page.close()
