import allure
from playwright.sync_api import Page


class W3SchoolPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_logo = page.get_by_label("Home link")
        self.main_input = page.get_by_placeholder("Search our tutorials, e.g.")
        self.not_sure_where_to_begin_link = page.get_by_role("link", name="Not Sure Where To Begin?")
        self.java_tutorial = page.get_by_role("link", name="JAVA", exact=True)
        self.java_boolean_section = page.get_by_role("link", name="Java Booleans")
        self.java_boolean_title = page.locator("h2").filter(has_text="Java Booleans")

    def get_w3_school_logo(self):
        return self.login_logo

    def get_main_input(self):
        return self.main_input

    def search_tutorials(self, topic_to_learn):
        self.main_input.fill(topic_to_learn)
        self.main_input.click()

    def not_sure_where_to_begin(self):
        return self.not_sure_where_to_begin_link

    @allure.step("Open Java tutorial page")
    def open_java_tutorial(self):
        self.java_tutorial.is_visible(timeout=3000)
        self.java_tutorial.click()

    @allure.step("Open Java boolean section")
    def open_java_boolean_section(self):
        self.java_boolean_section.is_enabled(timeout=3000)
        self.java_boolean_section.is_visible(timeout=3000)
        self.java_boolean_section.hover()
        self.java_boolean_section.click()

    def get_java_boolean_title(self):
        return self.java_boolean_title
