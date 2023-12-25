import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_user_go_to_w3school(set_up):
    page = set_up
    page.locator("xpath=//textarea[@class='gLFyf']").fill("w3schools")
    page.keyboard.press('Enter')
    page.locator("xpath=//h3[contains(text(),'W3Schools Online Web Tutorials')]").click()
    expect(page.locator("xpath=//input[@id='search2']")).to_be_visible(timeout=5000)

