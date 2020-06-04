from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_elements_by_tag_name("input")
    for element in x:
        element.send_keys("Hello")
        
    button = browser.find_element_by_css_selector("button.btn").click()
    
finally:
    time.sleep(5)
    browser.quit()
    