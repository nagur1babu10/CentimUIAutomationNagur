from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.find_element(by, value).click()

    def enter_text(self, by, value, text):
        elem = self.find_element(by, value)
        elem.clear()
        elem.send_keys(text)