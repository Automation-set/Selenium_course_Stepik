from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    # Scroll
    browser.execute_script("window.scrollBy(0, 200);")
    
    input1 = browser.find_element_by_id("answer").send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name("btn.btn-primary").click()
    
    
    
finally:
    time.sleep(5)
    browser.quit()

# Информация по скролу https://stepik.org/lesson/228249/step/5?unit=200781