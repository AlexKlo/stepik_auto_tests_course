from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

try:
    browser.get(link)
    #Говорим ждать 12 секунд, пока значение текста не станет равным $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR,"#price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
