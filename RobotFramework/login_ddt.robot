*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
Variables    ./data_variables.py
Resource    ./resource.robot
Test Setup    nopcommerce setup
Test Teardown    nopcommerce Teardown
Suite Setup    nopcommerce suite setup


*** Test Cases ***

Login to nopcommerce with username and password
    [tags]    tc3
    ${login_data}    Load testdata from excel    ./LoginData.xlsx    Sheet1
    Log    ${login_data}    console=True
    FOR   ${dt}   IN   @{login_data}
        ${status} =    Enter Username and Password    ${dt[0]}    ${dt[1]}
        Log    ${status}    console=True
        Run Keyword If    "${dt[2]}" =="Pass"    Verify Login nopcommerce if pass
        ...    ELSE IF    "${dt[2]}" =="Fail"    Title Should Be    Your store. Login
        ...    ELSE       FAIL
    END



