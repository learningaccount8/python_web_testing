import pytest
from playwright.sync_api import expect
from pom.login_page_elements import LoginPage


@pytest.mark.smoke
def test_user_go_to_base_page(set_up):
    page = set_up
    expect(page.get_by_role("link", name="Rozetka Logo")).to_be_visible()

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
