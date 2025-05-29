from pages.login_page import LoginPage
from utils.TestData import TestData
import pytest


@pytest.mark.smoke
@pytest.mark.sanity
def test_login_valid_user(driver):
    driver.get(TestData.url)
    login = LoginPage(driver)
    login.login(TestData.username, TestData.password)
    assert "My Account" in driver.page_source






@pytest.mark.nagur
@pytest.mark.sanity
def test_login_valid_user(driver):
    driver.get(TestData.url)
    login = LoginPage(driver)
    login.login(TestData.username, TestData.password)
    assert "My Account" in driver.page_source










@pytest.mark.Shaik
@pytest.mark.sanity
def test_login_valid_user(driver):
    driver.get(TestData.url)
    login = LoginPage(driver)
    login.login(TestData.username, TestData.password)
    assert "My Account" in driver.page_source