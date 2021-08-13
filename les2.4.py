import os, time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

abspath_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    browser.implicitly_wait(5)
    
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

    button = browser.find_element(By.ID,"book").click()
    x = browser.find_element(By.ID, 'input_value').text
    x = math.log(abs(12*math.sin(int(x))))
    browser.find_element(By.ID, 'answer').send_keys(str(x))
    button = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)
    button.click()



finally:
    time.sleep(5)
    browser.quit()