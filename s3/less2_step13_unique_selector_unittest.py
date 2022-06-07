import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestSeceltor(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        try:
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(1) input")
            input1.send_keys("A")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(2) input")
            input2.send_keys("K")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(3) input")
            input3.send_keys("stop_war@russia.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(expected_text, welcome_text, "Registration does not work!")
        finally:
            browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        try:
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(1) input")
            input1.send_keys("A")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(2) input")
            input2.send_keys("K")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(3) input")
            input3.send_keys("stop_war@russia.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(expected_text, welcome_text, "Registration does not work!")
        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()
