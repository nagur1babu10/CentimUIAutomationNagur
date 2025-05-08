from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.enter_text(By.ID, "username", username)
        self.enter_text(By.ID, "password", password)
        self.click(By.NAME, "login")

    def register(self, email, password):
        self.enter_text(By.ID, "reg_email", email)
        self.enter_text(By.ID, "reg_password", password)
        self.click(By.NAME, "register")