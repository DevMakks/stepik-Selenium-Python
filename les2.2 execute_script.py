from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    x_el = browser.find_element(By.ID,"input_value").text
    
    button = browser.find_element_by_tag_name("button")
    browser.find_element(By.ID,"answer").send_keys(calc(int(x_el)))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "robotsRule"))
    browser.find_element(By.ID, "robotsRule").click()
    button.click()
    
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(10)