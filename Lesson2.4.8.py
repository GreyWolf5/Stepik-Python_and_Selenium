from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pyperclip
import math

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_id("book").click()



y = calc(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()
#
alert = browser.switch_to.alert.text.split(': ')[-1]
print(alert)
pyperclip.copy(alert)

browser.quit()





# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
# browser.switch_to.window(new_window)

