from time import sleep

import pytest
import os
from hybrid_framework.PageObjects.LoginPageObj import Login
from hybrid_framework.Utilities.ReadProperty import Read_Property
from hybrid_framework.Utilities.CustomLogger import custom_logging
from hybrid_framework.Utilities.xlutility import *

class Test_Suite_Login_DDT:
    log = custom_logging()
    path = r".\TestData\LoginData.xlsx"
    sheet = 'Sheet1'
    # print(GetRow(path, sheet))
    # print(GetCol(path, sheet))
    login_data=[]
    for r in range(2, GetRow(path, sheet)+1):
        temp_list=[]
        for c in range(1,GetCol(path, sheet)+1):
            temp_list.append(ReadCell(path, sheet,r,c))
        #print(tuple(temp_list))
        login_data.append(tuple(temp_list))
    print(login_data)
    # [('admin@yourstore.com', 'admin', 'Pass'), ('admin@yourstore.com', 'adm', 'Fail'), ('adm@yourstore.com', 'admin', 'Fail'), ('adm@yourstore.com'
    # , 'adm', 'Fail')]
    @pytest.mark.functionality
    @pytest.mark.parametrize('user, pswd, expected', login_data)
    def test_verify_login_ddt(self, launch_browser, user, pswd, expected):
        driver = launch_browser
        log = custom_logging()
        self.log.info("Executing test_verify_dashbord")
        login_obj=Login(driver)
        login_obj.SetEmail(user)
        login_obj.SetPassword(pswd)
        login_obj.ClickSubmit()
        self.log.info("Successfully logged in to application...")
        self.log.info('jirra')

        status = login_obj.VerifyDashbord()
        print(status)
        if status == True and expected=="Pass":
            self.log.info("test_verify_dashbord[user:pswd:expected]:: PASSED")
            sleep(2)
            login_obj.ClickLogout()
            assert True
        elif status == False and expected=="Fail":
            self.log.info("test_verify_dashbord[user:pswd:expected]:: PASSED")
            assert True
        else:
            self.log.error("test_verify_dashbord[user:pswd:expected]:: FAILED")
            driver.save_screenshot(r'.\ScreenShots\test_verify_dashbord.png')
            assert False
