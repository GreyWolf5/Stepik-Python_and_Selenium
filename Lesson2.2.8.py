import os

import pyperclip as pyperclip
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_name("firstname").send_keys("name")
browser.find_element_by_name("lastname").send_keys("lastname")
browser.find_element_by_name("email").send_keys("email")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
browser.find_element_by_id("file").send_keys(file_path)
browser.find_element_by_class_name("btn").click()

alert = browser.switch_to.alert.text.split(': ')[-1]
print(alert)
pyperclip.copy(alert)

browser.quit()

