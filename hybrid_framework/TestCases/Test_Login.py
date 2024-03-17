from time import sleep

import pytest
import os
from hybrid_framework.PageObjects.LoginPageObj import Login
from hybrid_framework.Utilities.ReadProperty import Read_Property
from hybrid_framework.Utilities.CustomLogger import custom_logging
from hybrid_framework.TestData.test_data import *
import pytest_robotframework


class Test_Suite_Login:
    log = custom_logging()
    @pytest.mark.sanity
    def test_verify_title(self, launch_browser):

        self.log.info("Executing test_verify_title")
        driver = launch_browser
        self.log.info("Launching Browser...")
        if driver.title=="Your store. Login":
            self.log.info("test_verify_title::PASSED")
            assert True
        else:
            self.log.error("test_verify_title::FAILED")
            driver.save_screenshot(r'.\ScreenShots\test_verify_title.png')
            assert False

    @pytest.mark.sanity
    def test_verify_dashbord(self, launch_browser):
        driver = launch_browser
        log = custom_logging()
        self.log.info("Executing test_verify_dashbord")
        login_obj=Login(driver)
        # login_obj.SetEmail(Read_Property.GetUsername())
        # login_obj.SetPassword(Read_Property.GetPassword())
        login_obj.SetEmail(user)
        login_obj.SetEmail(password)
        login_obj.ClickSubmit()
        self.log.info("Successfully logged in to application...")
        self.log.info('jirra')

        status = login_obj.VerifyDashbord()

        if status == True:
            self.log.info("test_verify_dashbord:: PASSED")
            sleep(2)
            login_obj.ClickLogout()
            assert True
        else:
            self.log.error("test_verify_dashbord:: FAILED")
            driver.save_screenshot(r'.\ScreenShots\test_verify_dashbord.png')
            assert False
