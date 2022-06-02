from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotcheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsrule")
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
