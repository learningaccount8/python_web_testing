import allure
import pytest
from playwright.sync_api import expect
from pom.google_page import GooglePage
from pom.w3_school_page import W3SchoolPage
from utils.common_action import CommonActions


target_resource = "w3schools"


@pytest.mark.smoke
@allure.title("Test open W3School resource")
def test_open_w3school(set_up):
    page = set_up
    google_page = GooglePage(page)
    google_page.search_resource(target_resource)
    CommonActions.confirm_searching(page)
    google_page.open_w3_school_resource()

    expect(W3SchoolPage(page).get_w3_school_logo(), "The W3School logo should be visible").to_be_visible()


@pytest.mark.regression
@allure.title("Test open W3School resource/ Java section")
def test_open_java_boolean_section(set_up):
    page = set_up
    google_page = GooglePage(page)
    google_page.search_resource(target_resource)
    CommonActions.confirm_searching(page)
    google_page.open_w3_school_resource()
    w3_school_page = W3SchoolPage(page)

    expect(w3_school_page.get_main_input(), "The W3School main input should be visible").to_be_visible()
    w3_school_page.open_java_tutorial()
    w3_school_page.open_java_boolean_section()

    expect(w3_school_page.get_java_boolean_title(), "The W3School boolean title should be visible").to_be_visible()
