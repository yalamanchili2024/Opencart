import os.path
import time

from pageobjects.homepage import homepage
from pageobjects.loginpage import loginpage
from pageobjects.myaccount import myaccount
from utilities import XLutilis
from utilities.readproperties import readconfig


class Test_login_DDT:
    # writing the path where Excel sheet is located
    excel_path = "C:\\Users\\yalam\\PycharmProjects\\opecartv1\\Opencart\\testdata\\Opencart_logindata.xlsx"


    def test_login_ddt(self, setup):  # Getting the driver from conftest file  driver is in under
        self.driver = setup  # function name setup

        # getting all the rows from the Excel sheet -->  to read data from Excel we created the utilities file

        self.rows = XLutilis.getrowcount(self.excel_path, "Sheet1")
        lst_status = []  # this is list used to store all the status

        # Importing all page objects classes from POM
        self.hp = homepage(self.driver)
        self.lp = loginpage(self.driver)
        self.ma = myaccount(self.driver)

        self.driver.get(readconfig.applicationurl())
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        # Now we need to read data in the  row  from Excel sheet for that we need to use for loop

        for r in range(2, self.rows + 1):
            self.hp.clickmyaccount()
            self.hp.clicklogin()

            # Reading the data from the Excel sheet  by using XLutilis

            self.email = XLutilis.readdata(self.excel_path, "Sheet1", r, 1)
            self.password = XLutilis.readdata(self.excel_path, "Sheet1", r, 2)
            self.er = XLutilis.readdata(self.excel_path, "Sheet1", r, 3)

            self.lp.enter_email(self.email)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            time.sleep(5)
            self.targetpage = self.lp.target_page()

            if self.er == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.click_logout()

                else:
                    lst_status.append('Fail')

            elif self.er == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('fail')
                    time.sleep(10)
                    self.ma.click_logout()

                else:
                    lst_status.append('Pass')

        self.driver.close()

# Final validation  to check test case is pass or fail

        if "Fail" not in lst_status:
            assert True

        else:
            assert False

        print(lst_status)


