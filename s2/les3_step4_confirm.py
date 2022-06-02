from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
