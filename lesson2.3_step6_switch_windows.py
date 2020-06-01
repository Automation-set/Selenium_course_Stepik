from selenium import webdriver
import time
import math

link ="http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_tag_name("button").click()
    window2 = browser.window_handles[1]
    browser.switch_to.window(window2)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button").click()
    
    
    
finally:
    time.sleep(5)
    browser.quit()
    