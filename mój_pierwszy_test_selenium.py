from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# Inicjalizacja przeglądarki chrome
driver = webdriver.Chrome()

#Otwarcie okna przeglądarki
driver.get('https://www.google.pl')
accept = driver.find_element(by="xpath",value='//*[@id="L2AGLb"]')
accept.click()

#znajdz pole wyszukowania
search_box = driver.find_element('name','q')

#wprowadzenie hasła do wyszukiwania
search_box.send_keys('pogoda wrocław')

#naciśnij eneter
search_box.send_keys(Keys.ENTER)

#masykamlizacja okna
driver.maximize_window()
driver.set_window_size(1600,800)

#poczekaj 10 sekund, przed zamknięciem okna przeglądrki
#sleep tylko do celów debugowych, nauczania, testowania.
time.sleep(10)

#zakończ działanie przeglądarki
# driver.quit() #zamyka wszystkie okna w przeglądarce
driver.close  #zamyka dane okno w przeglądarce