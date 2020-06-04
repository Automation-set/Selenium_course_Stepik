from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
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
    
finally:
    time.sleep(8)
    browser.quit()
    