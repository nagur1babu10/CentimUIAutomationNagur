from pages.login_page import LoginPage
from utils.TestData import TestData
def test_login_valid_user(driver):
    driver.get(TestData.url)
    login = LoginPage(driver)
    login.login(TestData.username, TestData.password)
    assert "My Account" in driver.page_source