import allure
import pytest
from playwright.sync_api import expect

from pom.google_page import GooglePage
from pom.w3_school_page import W3SchoolPage
from pom.no_results_modal import NoResultsModal
from utils.common_action import CommonActions
from utils.constants import Constants


@pytest.mark.regression
@pytest.mark.parametrize("no_valid_test_data", [("dfdf"), ("543535"), ("*&&%$")])
@allure.title("Test open W3School resource/ Java section")
def test_open_java_boolean_section(set_up, no_valid_test_data):
    page = set_up
    google_page = GooglePage(page)
    google_page.search_resource(Constants.target_resource)
    CommonActions.confirm_searching(page)
    google_page.open_w3_school_resource()
    w3_school_page = W3SchoolPage(page)
    w3_school_page.search_tutorials(no_valid_test_data)

    if NoResultsModal(page).get_no_results_button().is_visible():
        NoResultsModal(page).no_results_click()

    expect(w3_school_page.not_sure_where_to_begin(), "No 'Not sure where to begin'").to_be_visible()