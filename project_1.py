import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://cat-fold.narod.ru/" #перешли на сайт
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

input1 = browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[1]/font/i/b/p[1]/a") #нашли раздел "Товары для животных"
browser.execute_script("return arguments[0].scrollIntoView(true);", input1) #проскроллили до раздела "Товары для животных"
text_input1 = input1.text #взяли текст "Товары для животных"
print(text_input1) #вывели на принт
assert text_input1 == 'Товары для животных' #ввели данные для сравнения
print('Good') #вывели на принт, что сравнение прошло успешно
input1.click() #нажали на кнопку раздела "Товары для животных"
time.sleep(10)

input2 = browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/p[5]/table/tbody/tr[2]/td[3]/p/i/b/a") #нашли раздел "Когтеточки"
browser.execute_script("return arguments[0].scrollIntoView(true);", input2) #проскроллили до раздела "Когтеточки"
time.sleep(5)
input2.click() #нажали на кнопку раздела "Когтеточки"
time.sleep(10)

input3 = browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/p[56]/a[2]/img") #нашли нужную картинку
browser.execute_script("return arguments[0].scrollIntoView(true);", input3) #проскроллили до картинки
time.sleep(5)
input3.click() #нажали на картинку, открыли ее
time.sleep(10)



# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()