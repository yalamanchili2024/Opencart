from selenium.webdriver.common.by import By


class accountregistrationpage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    firstname_txt_name = "firstname"
    lastname_txt_id = "input-lastname"
    email_txt_Xpath = '//*[@id="input-email"]'
    password_txt_cssselector = 'input[type="password"]'
    ppolicy_chk_xpath = '//*[@id="form-register"]/div/div/div/input'
    continue_button_xpath = '//*[@id="form-register"]/div/div/button'
    acccreation_notification_xpath = '//*[@id="content"]/h1'

    # Action Methods
    def enter_firstname(self, firstname):
        input_firstname = self.driver.find_element(By.NAME, self.firstname_txt_name)
        input_firstname.clear()
        input_firstname.send_keys(firstname)

    def enter_lastname(self, lastname):
        input_lastname = self.driver.find_element(By.ID, self.lastname_txt_id)
        input_lastname.clear()
        input_lastname.send_keys(lastname)

    def enter_email(self, email):
        input_email = self.driver.find_element(By.XPATH, self.email_txt_Xpath)
        input_email.clear()
        input_email.send_keys(email)

    def enter_password(self, password):
        input_password = self.driver.find_element(By.CSS_SELECTOR, self.password_txt_cssselector)
        input_password.clear()
        input_password.send_keys(password)

    def select_checkbox(self):
        hit_checkbox = self.driver.find_element(By.XPATH, self.ppolicy_chk_xpath)
        hit_checkbox.click()

    def click_continue(self):
        hit_continue = self.driver.find_element(By.XPATH, self.continue_button_xpath)
        hit_continue.click()

    def acc_confirmation(self):
        try:
            return self.driver.find_element(By.XPATH, self.acccreation_notification_xpath).text
        except Exception:
            print("Error Account is not created")
