import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link):
    url = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(url)
    answer = math.log(int(time.time()))
    time.sleep(5)
    input1 = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
    input1.send_keys(str(answer))
    time.sleep(5)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(5)
    elm_text = browser.find_element_by_class_name("smart-hints__hint")
    welcome_text = elm_text.text
    assert "Correct!" == welcome_text
    time.sleep(5)
