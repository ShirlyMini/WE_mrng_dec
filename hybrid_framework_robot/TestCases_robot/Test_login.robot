*** Settings ***
Library    Screenshot
Library    ../PageObjects/LoginPageObj.py
Library    ../Utilities/ReadProperty.py
#Library    ./conftest.py
Resource    ./resources.robot
Variables    ../TestData/test_data.py
Test Setup    NopCommerce setup    chrome
Test Teardown    NopCommerce teardown

*** Test Cases ***

Test1: Verify Title

    ${title} =    VerifyTitle    ${driver}
    Log     ${title}    console=True
    Take Screenshot   title


Test2: Verify Dashboard

    ${user} =    ReadProperty.GetUsername
    SetEmail    ${driver}    ${user}
    Take Screenshot   email
    ${pswd} =    ReadProperty.GetPassword
    SetPassword    ${driver}   ${pswd}
    Take Screenshot   password
    ClickSubmit    ${driver}
    Take Screenshot   submit
    ${title} =    VerifyTitle    ${driver}
#    Log     ${title}    console=True
    Run Keyword If   '${title}'!='Dashboard / nopCommerce administration'   Fail


