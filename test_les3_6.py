import time
import math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestMain():
    
    text = ""

    @pytest.mark.parametrize('link', [
                                    "https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"
                                    ]

                            )
    def test_answer_pass(self, link, browser):
        browser.get(link)
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
        browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        if element != "Correct!":
            self.text += element
            print(element)
    