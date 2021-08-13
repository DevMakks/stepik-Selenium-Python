from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    
    firstName = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required").send_keys("My Answer")
    lastName = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required").send_keys("My Answer")
    email = browser.find_element(By.CSS_SELECTOR, "input[class = \"form-control third\"]:required").send_keys("My Answer")
    button = browser.find_element(By.XPATH, "//button[contains(text(),\"Submit\")]").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()