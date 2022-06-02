from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    sum = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
