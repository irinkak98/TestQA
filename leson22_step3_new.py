import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome() # Загружаем браузер
browser.get(link) # Подставляем ссылку

num1 = browser.find_element(By.XPATH, '//*[@id="num1"]') # Находим элемент с первым числом
num2 = browser.find_element(By.XPATH, '//*[@id="num2"]') # Находим элемент со вторым числом

num1 = int(num1.text) # Получаем значение перового числа и переводим в целочисленный тип данных
num2 = int(num2.text) # Получаем значение второго числа и переводим в целочисленный тип данных

x = str(num1+num2) # Складываем значения первого и второго числа и переводим в строковый тип данных

spisok = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]')) # Находим выпадающий список
spisok.select_by_visible_text(x) # Выбираем нужный элемент списка

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button') # Находим кнопку
button.click() # Кликаем по кнопке
# закрываем браузер после всех манипуляций
time.sleep(30)
browser.quit()