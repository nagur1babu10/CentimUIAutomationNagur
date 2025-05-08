from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.TestData import TestData


@pytest.mark.regression
@pytest.mark.sanity
def test_add_address(driver):
    driver.get("https://practice.automationtesting.in/my-account/")
    login = LoginPage(driver)
    login.login("valid_user@example.com", "ValidPassword123")
    profile = ProfilePage(driver)
    profile.navigate_to_address_tab()
    profile.edit_billing_address()
    profile.update_address("John", "Doe", "123 Testing St")
    assert "Address changed successfully" in driver.page_source
