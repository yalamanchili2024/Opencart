import os
import time

import pytest

from pageobjects.homepage import homepage
from pageobjects.loginpage import loginpage
from utilities.readproperties import readconfig


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class Test_002_userlogin:

    @pytest.mark.sanity
    def test_user_login(self, setup):  # driver setup from conftest file
        self.driver = setup
        self.driver.implicitly_wait(10)
        # Opening application url by using method in read proprieties which is the value form config file

        self.driver.get(readconfig.applicationurl())
        self.driver.maximize_window()
        time.sleep(10)

        # Creating the object for the homepage POM to use home page pom in this test case

        self.hp = homepage(self.driver)
        self.hp.clickmyaccount()
        self.hp.clicklogin()
        time.sleep(10)

        # Creating the object for the login page POM to use login page pom in this test case

        self.lp = loginpage(self.driver)
        self.lp.enter_email(readconfig.useremail())
        self.lp.enter_password(readconfig.userpassword())
        self.lp.click_login()

        # After login  validating weather login page information is displayed or not ?

        if self.lp.target_page:
            assert True
        else:
            screenshot = os.path.join(r"C:\Users\yalam\PycharmProjects\opecartv1\Opencart\screenshots",
                                      " test_user_login.png")
            assert False

        self.driver.close()
