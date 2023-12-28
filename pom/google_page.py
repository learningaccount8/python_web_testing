import allure
from playwright.sync_api import Page


class GooglePage:

    def __init__(self, page: Page):
        self.page = page
        self.searchInput = page.locator("xpath=//textarea[@class='gLFyf']")
        self.w3schoolLink = page.locator("xpath=//h3[contains(text(),'W3Schools Online Web Tutorials')]")

    @allure.step("Searching the resource (resource_to_find: {resource_to_find})")
    def search_resource(self, resource_to_find):
        self.searchInput.fill(resource_to_find)

    @allure.step("Confirm the searching resource")
    def open_w3_school_resource(self):
        self.w3schoolLink.click()


