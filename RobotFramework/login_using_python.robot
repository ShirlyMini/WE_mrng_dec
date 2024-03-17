*** Settings ***
#Library    SeleniumLibrary
Library    Screenshot
Variables    ./data_variables.py
Resource    ./resource.robot
Library    ./PageObjects/LoginPageObj.py
Library    ./PageObjects/conftest.py
#Test Setup    nopcommerce setup
#Test Teardown    nopcommerce Teardown
#Suite Setup    nopcommerce suite setup

*** Test Cases ***

Login to nopcommerce with username and password
    [tags]    tc3
    ${driver}    launch_browser    chrome
    SetEmail    ${driver}    ${cred['username']}
    SetPassword    ${driver}    ${cred['password']}
    ClickSubmit    ${driver}
    ClickLogout    ${driver}
