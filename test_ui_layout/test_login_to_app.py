import pytest
from playwright.sync_api import expect
from pom.login_page_elements import LoginPage


@pytest.mark.smoke
def test_user_go_to_base_page(set_up):
    page = set_up
    expect(page.get_by_role("link", name="Rozetka Logo")).to_be_visible()


@pytest.mark.smoke
def test_user_go_to_base_page2(set_up):
    page = set_up
    page.locator("xpath=//input[@class='search-form__input ng-untouched ng-pristine ng-valid']").fill("samsung s23")
    page.locator("xpath=//button[@class='button button_color_green button_size_medium search-form__submit']").click()
    page.wait_for_selector(page.get_by_role("link", name="Rozetka Logo")).to_be_visible()


@pytest.mark.smoke
def test_user_go_to_base_page3(set_up):
    page = set_up
    page.locator("xpath=//textarea[@class='gLFyf']").fill("w3schools")
    page.keyboard.press('Enter')
    page.locator("xpath=//h3[contains(text(),'W3Schools Online Web Tutorials')]").click()
    expect(page.locator("xpath=//input[@id='search2']")).to_be_visible(timeout=5000)


@pytest.mark.regression
@pytest.mark.parametrize("user_login,user_password", [("1111", "6765675")])#, ("hjjh", "hjhghghf"), ("&^%$", "&*&$#")])
def test_user_login_with_invalid_data(set_up, user_login, user_password) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open_login_modal()
    login_page.fill_out_user_data(user_login, user_password)
    login_page.confirm()

    expect(page.get_by_text("Введено невірну адресу ел. пошти або номер телефону"),
           "The error message should be visible").to_be_visible()

