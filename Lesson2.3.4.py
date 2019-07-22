from selenium import webdriver
import pyperclip as pyperclip
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element_by_class_name("btn").click()
browser.switch_to.alert.accept()

y = calc(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_class_name("btn").click()

alert = browser.switch_to.alert.text.split(': ')[-1]
print(alert)
pyperclip.copy(alert)

browser.quit()
