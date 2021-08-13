import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

abspath_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'file.txt')
# element.send_keys(file_path)

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    browser.find_element(By.NAME, 'firstname').send_keys("Maksim")
    browser.find_element(By.NAME, 'lastname').send_keys("Test")
    browser.find_element(By.NAME, 'email').send_keys("Test@email.com")
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CLASS_NAME,'btn.btn-primary').click()


finally:
    time.sleep(5)
    browser.quit()