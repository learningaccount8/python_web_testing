import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_user_go_to_w3school(set_up):
    page = set_up
    page.locator("xpath=//textarea[@class='gLFyf']").fill("w3schools")
    page.keyboard.press('Enter')
    # page.get_by_text("w3schools", exact=True).click()
    page.locator("xpath=//h3[contains(text(),'W3Schools Online Web Tutorials')]").click()
    expect(page.locator("xpath=//input[@id='search2']")).to_be_visible()
    page.get_by_role("link", name="JAVA", exact=True).click()
    page.locator("xpath=//a[contains(text(),'Java Booleans')]").is_enabled(timeout=5000)
    page.locator("xpath=//a[contains(text(),'Java Booleans')]").click()
    expect(page.get_by_role("heading", name="Boolean Values")).to_be_visible()

