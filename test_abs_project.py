import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def test_lesson16_step10_assert(self):
        browser = webdriver.Chrome()
        browser.get(self.link1)

        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys("Hello")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys("Hello")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys("Hello")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(3)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_lesson16_step10_assert_false(self):
        browser = webdriver.Chrome()
        browser.get(self.link2)

        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys("Hello")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys("Hello")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys("Hello")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(3)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    unittest.main()
