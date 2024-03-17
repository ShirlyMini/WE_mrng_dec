*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
Variables    ./data_variables.py
Resource    ./resource.robot
Test Setup    nopcommerce setup
Test Teardown    nopcommerce Teardown
Suite Setup    nopcommerce suite setup
#Suite Teardown

#*** Variables ***
#${url}   https://admin-demo.nopcommerce.com/
#${exe_path}    E:/selenium/drivers/chromedriver.exe

*** Test Cases ***
Login to nopcommerce
    [tags]    tc1
#    [Setup]    nopcommerce setup
#    Set Log level   Trace
#    Open Browser   ${url}    chrome    executable_path=${exe_path}
#    Maximize Browser Window
    Title Should Be    Your store. Login
    Take Screenshot    loginpage
#    [teardown]    nopcommerce Teardown

Login to nopcommerce with username and password
    [tags]    tc2
#    [Setup]    nopcommerce setup
#    Input Text    id:Email    ${cred['username']}
#    Input Password    id:Password    ${cred['password']}
#    Click Element    xpath://button[@type='submit']
    ${status} =    Enter Username and Password    ${cred['username']}    ${cred['password']}
    Log    ${status}    console=True
    Title Should Be    Dashboard / nopCommerce administration
#    [teardown]    nopcommerce Teardown


