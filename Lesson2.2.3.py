from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
# browser.get("http://suninjuly.github.io/selects2.html")

x = int(browser.find_element_by_id("num1").text)
y = int(browser.find_element_by_id("num2").text)
z = str(x + y)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(z)

browser.find_element_by_class_name("btn").click()

alert = browser.switch_to_alert()
print(alert.text)

browser.quit()
