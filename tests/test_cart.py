import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.TestData import TestData




@pytest.mark.smoke
def test_add_and_remove_from_cart(driver):
    home = HomePage(driver)
    cart = CartPage(driver)
    driver.get("https://practice.automationtesting.in/shop/")
    home.add_first_product_to_cart()
    home.go_to_cart()
    assert cart.get_cart_count() > 0