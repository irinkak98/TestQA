import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
input1.click()
time.sleep(1)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input2 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input2.send_keys(y)
time.sleep(1)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()





# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()