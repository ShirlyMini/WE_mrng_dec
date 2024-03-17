*** Settings ***
Library    ./conftest.py

*** Keywords ***

NopCommerce setup
    [arguments]    ${browser}
    Set Log level   Trace
    ${driver} =    launch_browser    ${browser}
#    [return]    ${driver}
    Set Test Variable   ${driver}

NopCommerce teardown
    browser_teardown    ${driver}
