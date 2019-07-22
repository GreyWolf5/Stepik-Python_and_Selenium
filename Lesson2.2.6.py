from selenium import webdriver

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("robotCheckbox").click()

radio = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
# button.click()


browser.find_element_by_id("robotsRule").click()
browser.find_element_by_class_name("btn").click()

alert = browser.switch_to_alert()
print(alert.text)

browser.quit()


