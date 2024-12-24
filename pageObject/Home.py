from selenium.webdriver.common.by import By
from pageObject.Checkout import CheckOutPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    #(By.XPATH, "//a[contains(@href,'shop')]")
    myname = (By.CSS_SELECTOR, "input[name='name']")
    myemail = (By.NAME, "email")
    mypassword = (By.ID, "exampleInputPassword1")
    mycheck = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submitB = (By.XPATH,"//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)

    def inputName(self):
        return self.driver.find_element(*HomePage.myname)

    def inputEmail(self):
        return self.driver.find_element(*HomePage.myemail)

    def inputPassword(self):
        return self.driver.find_element(*HomePage.mypassword)

    def makeCheck(self):
        return self.driver.find_element(*HomePage.mycheck)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submitB)

    def messageText(self):
        return self.driver.find_element(*HomePage.message)