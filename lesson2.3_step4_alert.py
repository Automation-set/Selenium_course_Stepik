from selenium import webdriver 
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_class_name("btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_class_name("btn.btn-primary").click()
    
finally:
    time.sleep(5)
    browser.quit()
    