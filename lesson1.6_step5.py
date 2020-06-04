from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    link = browser.find_element_by_link_text("224592")
    link.click()
    input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
    input2=browser.find_element_by_name("last_name").send_keys("Petrov")
    input3=browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")
    input4=browser.find_element_by_id("country").send_keys("Russia")
    Button=browser.find_element_by_css_selector("button.btn").click()
 
    
finally:
	time.sleep(30)
	browser.quit()

