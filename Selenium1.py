from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.set_window_size(1600,800)
time.sleep(4)
try:
    username_field = driver.find_element('xpath','//*[@id="user-named"]')
except:
    print('nie znaleziono pola "user-named" po xpath. Szukam po nazwie')
    username_field = driver.find_element('name', 'user-name')

username_field.clear()
username_field.send_keys('standard_user')
password_field = driver.find_element(By.XPATH,'//*[@id="password"]')
password_field.send_keys('secret_sauce')

login_button = driver.find_element(By.NAME,'login-button')
if not login_button.get_attribute('disable'):
    login_button.click()
else:
    print('przycisk nieaktywny')
time.sleep(3)
driver.get_screenshot_as_file('screen.png')
make_screenshot(driver)

driver.quit