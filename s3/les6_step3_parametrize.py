import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

#answer = math.log(int(time.time()))
link_nums = [str(236895+i) for i in range(5)]
link_nums += [str(236903+i) for i in range(3)]

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestAlienMessage():

    @pytest.mark.parametrize('number', link_nums)
    def test_answer(self, browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        input = browser.find_element(By.CLASS_NAME, "ember-text-area")
        input.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")

        assert message.text == "Correct!", f"Secret message: {message.text}"
