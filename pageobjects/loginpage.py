from selenium.webdriver.common.by import By


class loginpage:
    # Constructor

    def __init__(self, driver):
        self.driver = driver

    #locators

    emailaddress_txt_xpath = '//*[@id="input-email"]'
    password_txt_cssselector = 'input[name="password"]'
    login_button_cssselector = 'button[type="submit"]'
    loginconfirmation_page_xpath = '//*[@id="content"]/h2[1]'

    # Action Methods

    def enter_email(self, email):
        email_box = self.driver.find_element(By.XPATH, self.emailaddress_txt_xpath)
        email_box.clear()
        email_box.send_keys(email)

    def enter_password(self, password):
        password_box = self.driver.find_element(By.CSS_SELECTOR, self.password_txt_cssselector)
        password_box.clear()
        password_box.send_keys(password)

    def click_login(self):
        login = self.driver.find_element(By.CSS_SELECTOR, self.login_button_cssselector)
        login.click()

    def target_page(self):
        try:
            return self.driver.find_element(By.XPATH, self.loginconfirmation_page_xpath).is_displayed()
        except:
            return False

    def email_locator(self):
        return self.driver.find_element(By.XPATH, self.emailaddress_txt_xpath)
