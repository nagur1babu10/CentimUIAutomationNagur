from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def add_first_product_to_cart(self):
        self.click(By.CLASS_NAME, "add_to_cart_button")

    def go_to_cart(self):
        self.click(By.CLASS_NAME, "cartcontents")