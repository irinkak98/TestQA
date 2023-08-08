import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
num1 = int(num1)
num2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
num2 = int(num2)
value = str(num1 + num2)
print('num1+num2=', value)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(value) #нашли искомый элемент

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()



# закрываем браузер после всех манипуляций
time.sleep(30)
browser.quit()