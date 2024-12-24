from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver
    country1 = (By.ID, "country")
    country2 = (By.XPATH, "//a[contains(text(),'India')]")
    check = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def countrySearch(self):
        return  self.driver.find_element(*ConfirmPage.country1)

    def countryConfirm(self):
        return self.driver.find_element(*ConfirmPage.country2)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.check)

    def submitB(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def alertSuccess(self):
        return self.driver.find_element(*ConfirmPage.alert)