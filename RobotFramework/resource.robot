*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
Library    ./xlutility.py
Library    Collections

*** Keywords ***
nopcommerce setup
    Open Browser   ${url}    chrome    executable_path=${exe_path}
    Maximize Browser Window

nopcommerce Teardown
    Close All Browsers

nopcommerce suite setup
    Set Log level   Trace

Enter Username and Password
    [Arguments]    ${usr}    ${pswd}
    Input Text    id:Email    ${usr}
    Input Password    id:Password   ${pswd}
    Click Element    xpath://button[@type='submit']
    RETURN    True

Load testdata from excel
    [arguments]    ${path}    ${sheet}
#    ${data}    Create List
#    ${no_row}    xlutility.GetRow   ${path}    ${sheet}
#    ${no_col}    xlutility.GetCol   ${path}    ${sheet}
#    FOR    ${r}    IN RANGE    2    ${no_row}+1
#        ${temp_data}    Create List
#        FOR    ${c}    IN RANGE    1    ${no_col}+1
#            ${val}    xlutility.ReadCell     ${path}    ${sheet}   ${r}    ${c}
#            Append To List    ${temp_data}    ${val}
#        END
#        Append To List    ${data}    ${temp_data}
#    END
    ${data}    xlutility.load_test_data_from_xl    ${path}    ${sheet}
    RETURN    ${data}

Verify Login nopcommerce if pass
    Title Should Be    Dashboard / nopCommerce administration
    Click Element    xpath://a[contains(text(),'Logout')]