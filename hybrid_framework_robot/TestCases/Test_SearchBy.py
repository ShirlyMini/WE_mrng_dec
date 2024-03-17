from time import sleep

import pytest
from hybrid_framework.PageObjects.LoginPageObj import Login
from hybrid_framework.PageObjects.SearchBy_PageObj import SearchBy
from hybrid_framework.Utilities.ReadProperty import Read_Property
from hybrid_framework.Utilities.CustomLogger import custom_logging
from hybrid_framework.TestData.test_data import *

class Test_SearchBy_Functionality:
    log = custom_logging()

    @pytest.mark.sanity
    def test_searchby_email(self, launch_browser):

        self.log.info("Executing test_serchby_email")
        driver = launch_browser
        self.log.info("Launching Browser...")
        login_obj = Login(driver)
        login_obj.SetEmail(Read_Property.GetUsername())
        login_obj.SetPassword(Read_Property.GetPassword())
        login_obj.ClickSubmit()
        self.log.info("Successfully logged in to application...")

        search_obj = SearchBy(driver)
        search_obj.NavigateToCustomerMenu()
        search_obj.SearchEmail("james_pan@nopCommerce.com")
        search_obj.ClickSearch()
        sleep(5)
        output_list= search_obj.GetEmailColumn()
        self.log.info(f"Successfully searched item...{output_list}")

        if "james_pan@nopCommerce.com" in output_list:
            self.log.info("test_searchby_email:: PASSED")
            assert True
        else:
            self.log.error("test_searchby_email:: FAILED")
            driver.save_screenshot(r'.\ScreenShots\test_searchby_email.png')
            assert False

    @pytest.mark.functionality
    @pytest.mark.parametrize("name", search_name['firstname'])
    def test_searchby_firstname(self, launch_browser, name):

        self.log.info("Executing test_searchby_firstname")
        driver = launch_browser
        self.log.info("Launching Browser...")
        login_obj = Login(driver)
        login_obj.SetEmail(Read_Property.GetUsername())
        login_obj.SetPassword(Read_Property.GetPassword())
        login_obj.ClickSubmit()
        self.log.info("Successfully logged in to application...")

        search_obj = SearchBy(driver)
        search_obj.NavigateToCustomerMenu()
        search_obj.SearchFirstname(name)
        search_obj.ClickSearch()
        sleep(5)
        output_list= search_obj.GetNameColumn()
        self.log.info(f"Successfully searched item...{output_list}")

        for output in output_list:
            if name in output:
                self.log.info("test_searchby_firstname:: PASSED")
                assert True
            else:
                self.log.error("test_searchby_firstname:: FAILED")
                driver.save_screenshot(r'.\ScreenShots\test_searchby_firstname.png')
                assert False

    @pytest.mark.functionality
    @pytest.mark.parametrize("name", search_name['lastname'])
    def test_searchby_lastname(self, launch_browser, name):

        self.log.info("Executing test_searchby_lastname")
        driver = launch_browser
        self.log.info("Launching Browser...")
        login_obj = Login(driver)
        login_obj.SetEmail(Read_Property.GetUsername())
        login_obj.SetPassword(Read_Property.GetPassword())
        login_obj.ClickSubmit()
        self.log.info("Successfully logged in to application...")

        search_obj = SearchBy(driver)
        search_obj.NavigateToCustomerMenu()
        search_obj.SearchLastname(name)
        search_obj.ClickSearch()
        sleep(5)
        output_list = search_obj.GetNameColumn()
        self.log.info(f"Successfully searched item...{output_list}")

        for output in output_list:
            if name in output:
                self.log.info("test_searchby_lastname:: PASSED")
                assert True
            else:
                self.log.error("test_searchby_lastname:: FAILED")
                driver.save_screenshot(r'.\ScreenShots\test_searchby_lastname.png')
                assert False