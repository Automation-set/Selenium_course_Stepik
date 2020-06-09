from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
    input1.send_keys(str(answer))
    time.sleep(5)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(60)

finally:
    browser.quit()
