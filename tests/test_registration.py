from pages.login_page import LoginPage
import uuid
from utils.TestData import TestData



@pytest.mark.regression
@pytest.mark.sanity
def test_user_registration(driver):
    driver.get("https://practice.automationtesting.in/my-account/")
    login = LoginPage(driver)
    unique_email = f"user_{uuid.uuid4().hex[:6]}@test.com"
    login.register(unique_email, "TestPassword123!")
    assert "My Account" in driver.page_source