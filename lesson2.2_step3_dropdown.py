from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    z = str(int(x)+int(y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
    time.sleep(1)
    button = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(5)
    browser.quit()