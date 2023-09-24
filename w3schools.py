from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# Inicjalizacja przeglądarki chrome
driver = webdriver.Chrome()

#Otwarcie okna przeglądarki
driver.get('https://www.w3schools.com')
print('tutuł bieżącego okna przeglądarki to:', driver.title)


#masykamlizacja okna
driver.maximize_window()
driver.set_window_size(1600,800)
#accept = driver.find_element(by='id', value='//*[@id="top-nav-bar"]')

#poczekaj 10 sekund, przed zamknięciem okna przeglądrki
#sleep tylko do celów debugowych, nauczania, testowania.
time.sleep(100)

#zakończ działanie przeglądarki
# driver.quit() #zamyka wszystkie okna w przeglądarce
driver.close  #zamyka dane okno w przeglądarce