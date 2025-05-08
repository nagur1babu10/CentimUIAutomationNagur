from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfilePage(BasePage):
    def navigate_to_address_tab(self):
        self.click(By.LINK_TEXT, "Addresses")

    def edit_billing_address(self):
        self.click(By.LINK_TEXT, "Edit")

    def update_address(self, first_name, last_name, address):
        self.enter_text(By.ID, "billing_first_name", first_name)
        self.enter_text(By.ID, "billing_last_name", last_name)
        self.enter_text(By.ID, "billing_address_1", address)
        self.click(By.NAME, "save_address")