import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "http://chelbus.ru/" #перешли на сайт
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
time.sleep(5)

input1 = browser.find_element(By.XPATH, '/html/body/header/div/div/div/div[3]/div/nav/ul/li[3]/a') #перешли в раздел "Другие города"
input1.click() #нажали на кнопку
time.sleep(5)

input2 = browser.find_element(By.XPATH, '//*[@id="top-menu"]/ul/li[2]/a') #нашли выпадающее окно "Расписание"
input2.click() #нажали на кнопку "Раcписание", открылся выпадающий список (фильтр)
time.sleep(5)
input2.send_keys(Keys.DOWN) #это срабатывает
time.sleep(5)
input2.send_keys(Keys.RETURN) #видимо так как не фильтр, а конкретные страницы - не переходит

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()