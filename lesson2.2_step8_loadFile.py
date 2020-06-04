from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname").send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname").send_keys("Ivanovich")
    input3 = browser.find_element_by_name("email").send_keys("123@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__)) #current_dir - обозначение; os.path.abspath - функция, мы
    file = os.path.join(current_dir, 'file.txt') #
    input4 = browser.find_element_by_id("file").send_keys(file)
    button = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(5)
    browser.quit()
    # Информация по вставке файлов https://stepik.org/lesson/228249/step/7?unit=200781
    