from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Что-то пошло не так")

    def test_reg2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Что-то пошло не так")


if __name__ == "__main__":
    unittest.main()
