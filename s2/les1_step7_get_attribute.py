from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    img = browser.find_element(By.ID, "treasure")
    x = img.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotcheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsrule")
    radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
