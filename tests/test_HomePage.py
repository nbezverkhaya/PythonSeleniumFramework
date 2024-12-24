import time
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestData.HomePageData import HomePageData
from pageObject.Home import HomePage
from utilities.BaseCless import BaseClass
service_obj = Service(ChromeDriverManager().install())

class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.inputName().send_keys(getData["firstname"])
        homepage.inputEmail().send_keys(getData["email"])
        homepage.inputPassword().send_keys(getData["password"])
        homepage.makeCheck().click()
        self.selectOptionByText(homepage.selectGender(), getData["gender"])
        homepage.clickSubmit().click()
        message = homepage.messageText().text
        assert ("Success!" in message)
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase3")
    def getData(self, request):
        return request.param

