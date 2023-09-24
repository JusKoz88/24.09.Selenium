*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Log In Wikipedia
    Open Browser    https://pl.wikipedia.org    chrome
    Click Element    id:pt-login-2
    Input Text    id:wpName1    RobotTests
    Input Password    id:wpPassword1    RobotFramework
    Click Button     id:wpLoginAttempt
    Sleep  3