import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://kinodivbox.github.io/" #перешли на сайт
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

input1 = browser.find_element(By.XPATH, '//*[@id="search-title"]') #нашли поле для ввода фильма для поиска
input1.send_keys('Круэлла') #вводим искомый фильм
time.sleep(10)

input2 = browser.find_element(By.XPATH, '//*[@id="search"]') #кнопка "Найти"
input2.click() #нажали на кнопку "Найти"

# закрываем браузер после всех манипуляций
time.sleep(240)
browser.quit()