import os
import time

import pytest

from pageobjects.accountregistrationpage import accountregistrationpage
from pageobjects.homepage import homepage
from utilities import randomestring
from utilities.readproperties import readconfig


class Test_001_accountReg:
    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(readconfig.applicationurl())  # used config file data to enter the website URL
        # here read config is the  class name in the read properties file. and application url is the method inside
        # the class like this we need to use the class and method to read values
        self.driver.maximize_window()
        time.sleep(2)

        self.HP = homepage(self.driver)  # Homepage is the POM, and I created an object name self.HP,
        # and  we need to pass the driver when ever we created the object for POM
        self.driver.implicitly_wait(10)
        self.HP.clickmyaccount()
        self.HP.clickregister()
        time.sleep(10)

        self.ARP = accountregistrationpage(self.driver)
        self.ARP.enter_firstname("sam")
        self.ARP.enter_lastname("tom")

        # self.ARP.enter_email('zkfay8@gmail.com')
        # In this particular scenario every time we run the script we need to enter the new email which is
        # not possible manually,so we need to create a utility file to generate the random unique email every time

        self.email = randomestring.random_string_generator() + '@gmail.com'  # utility file created for this
        self.ARP.enter_email(self.email)
        # self.ARP.enter_email(readconfig.useremail())  # used config file data to enter the email address
        self.ARP.enter_password(readconfig.userpassword())  # used config file data to enter the password
        time.sleep(5)
        self.ARP.select_checkbox()
        self.ARP.click_continue()
        self.cnf = self.ARP.acc_confirmation()
        print(self.cnf)  # Print confirmation message for debugging
        time.sleep(5)
        if self.cnf == "Register Account":
            assert True
        else:  # below is the path used to save the screenshots  os.path.join

            screenshot_path = os.path.join(r"C:\Users\yalam\PycharmProjects\opecartv1\Opencart\screenshots",
                                           "test_account_reg.png")
            self.driver.save_screenshot(screenshot_path)
            assert False
