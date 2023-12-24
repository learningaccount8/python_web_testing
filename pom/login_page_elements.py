from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.login_logo = page.get_by_role("link", name="Rozetka Logo")
        self.accountButton = page.locator("rz-user").get_by_role("button")
        self.userLoginInput = page.get_by_label("Ел. пошта або телефон")
        self.userPasswordInput = page.get_by_label("Пароль")
        self.confirmButton = page.get_by_role("button", name="Увійти")

    def open_login_modal(self):
        self.accountButton.click()

    def fill_out_user_data(self, user_login, user_password):
        self.userLoginInput.fill(user_login)
        self.userPasswordInput.fill(user_password)

    def confirm(self):
        self.confirmButton.click()

    def is_error_appears(self):
        self.page.get_by_text("Введено невірну адресу ел. пошти або номер телефону")
