from playwright.sync_api import Page


class CommonActions:

    @staticmethod
    def confirm_searching(page: Page):
        page.keyboard.press('Enter')