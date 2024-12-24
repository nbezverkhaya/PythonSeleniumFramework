from selenium.webdriver.common.by import By
from pageObject.Confirm import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    cardTitles = (By.XPATH, '//div[@class="card h-100"]')
    cardFooter1 = (By.XPATH, '//div/h4/a')
    cardFooter2 = (By.XPATH, 'div/button') #(By.XPATH, 'div[2]/button')
    primaryButton = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')
    checkOutB = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCardFooter1(self):
        return self.driver.find_element(*CheckOutPage.cardFooter1)

    def getCardFooter2(self):
        return self.driver.find_element(*CheckOutPage.cardFooter2)

    def clickPrimary(self):
        return self.driver.find_element(*CheckOutPage.primaryButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutB).click()
        return ConfirmPage(self.driver)