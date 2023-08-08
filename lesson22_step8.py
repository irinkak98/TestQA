import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
input1.send_keys('Ivan')

input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
input2.send_keys('Petrov')

input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
input3.send_keys('123@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
input4.send_keys(file_path)

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()