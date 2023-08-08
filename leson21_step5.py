from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)
time.sleep(2)

check_box = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
check_box.click()
time.sleep(2)

radio_button = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
radio_button.click()
time.sleep(2)

submit = browser.find_element(By.XPATH, "//button[@type='submit']")
submit.click()



    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()