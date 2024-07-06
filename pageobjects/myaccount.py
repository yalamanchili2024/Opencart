from selenium.webdriver.common.by import By


class myaccount:
    # constructor

    def __init__(self,driver):
        self.driver = driver

    # locators

    logout_drpvalue_cssselector = "a.dropdown-item[href='https://demo.opencart.com/index.php?route=account/logout&language=en-gb']"

    # Action methods

    def click_logout(self):
        logout = self.driver.find_element(By.CSS_SELECTOR, self.logout_drpvalue_cssselector)
        logout.click()
