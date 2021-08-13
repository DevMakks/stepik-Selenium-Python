import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    x_element = browser.find_element(By.ID,"treasure").get_attribute("valuex")
    assert browser.find_element(By.ID,"peopleRule").get_attribute("checked") == "true", "People radio isn't selected by default"
    assert browser.find_element(By.ID,"robotsRule").get_attribute("checked") != "true"
    assert browser.find_element(By.CSS_SELECTOR,"button.btn.btn-default").get_attribute("disabled") != "true"
    
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(calc(x_element)))
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    

finally:
    time.sleep(10)
    browser.quit()