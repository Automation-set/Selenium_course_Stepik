from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer").send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_css_selector("[class='btn btn-default']").click()
    
finally:
    time.sleep(5)
    browser.quit()
    