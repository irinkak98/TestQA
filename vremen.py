import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

input2 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
input2.click()

input3 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
input3.click()

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button.click()

time.sleep(5)
browser.quit()