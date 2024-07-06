from selenium.webdriver.common.by import By

class homepage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    myaccount_dropdown_xpath = '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span'
    register_dropdownitem_xpath = '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a'
    login_dropdownitem_partiallinktext = "Login"

    # Action methods
    def clickmyaccount(self):
        clickmyaccount = self.driver.find_element(By.XPATH, self.myaccount_dropdown_xpath)
        clickmyaccount.click()

    def clickregister(self):
        clickregister = self.driver.find_element(By.XPATH, self.register_dropdownitem_xpath)
        clickregister.click()

    def clicklogin(self):
        clicklogin = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.login_dropdownitem_partiallinktext)
        clicklogin.click()
