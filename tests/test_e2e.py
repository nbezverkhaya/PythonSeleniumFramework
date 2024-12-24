import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObject.Checkout import CheckOutPage
from pageObject.Home import HomePage
from pageObject.Confirm import ConfirmPage
from utilities.BaseCless import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    driver: WebDriver

    def test_e2e(self, setup):
        log = self.getLogger()
        checkoutPage = HomePage(self.driver).shopItems() #CheckOutPage(self.driver) object
        log.info("getting all the shop item names")
        time.sleep(2)
        elList = checkoutPage.getCardTitles()
        for e in elList:
            log.info(f"Item name: {e.text}")
            el = checkoutPage.getCardFooter1()
            if "Blackberry" in el.text:
                e.checkOutP.getCardFooter2().click()
        checkoutPage.clickPrimary().click()
        time.sleep(2)

        confirmP = CheckOutPage(self.driver).checkOutItems() #ConfirmPage(self.driver) object
        log.info("Entering country name as ind")
        confirmP.countrySearch().send_keys("ind")
        self.verifyLinkPresence(ConfirmPage.country2)
        confirmP.countryConfirm().click()
        confirmP.checkBox().click()
        confirmP.submitB().click()
        successText = confirmP.alertSuccess().text
        log.info("text received from alert "+successText)

        assert "Success! Thank you!" in successText