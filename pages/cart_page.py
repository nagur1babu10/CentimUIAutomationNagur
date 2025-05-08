from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def get_cart_count(self):
        count_text = self.find_element(By.CLASS_NAME, "cartcontents").text
        return int(count_text.split()[0]) if count_text else 0

    def proceed_to_checkout(self):
        self.click(By.CLASS_NAME, "checkout-button")