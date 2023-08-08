import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
input1.click()

alert = browser.switch_to.alert
alert.accept()

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input2 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input2.send_keys(y)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()





# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()