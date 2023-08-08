import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB" #перешли на сайт
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
time.sleep(5)

# alert = browser.switch_to.alert
# alert.accept()

input2 = browser.find_element(By.XPATH, '//*[@id="input_11_10"]') #нашли выпадающее окно
browser.execute_script("return arguments[0].scrollIntoView(true);", input2) #проскроллили до раздела
input2.click() #нажали на кнопку, открылся выпадающий список (фильтр)
time.sleep(5)

select = Select(browser.find_element(By.TAG_NAME, 'select')) #поиск выпадающего списка
select.select_by_visible_text("Cyprus") # ищем элемент с текстом


# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()