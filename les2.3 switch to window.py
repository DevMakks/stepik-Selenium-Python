import os, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

abspath_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'file.txt')
# element.send_keys(file_path)

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.implicitly_wait(5)
    
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    browser.switch_to_window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    x = math.log(abs(12*math.sin(int(x))))
    browser.find_element(By.ID, 'answer').send_keys(str(x))
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()



finally:
    time.sleep(5)
    browser.quit()