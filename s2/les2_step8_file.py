from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name=\"firstname\"]")
    input1.send_keys("A")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name=\"lastname\"]")
    input2.send_keys("K")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name=\"email\"]")
    input3.send_keys("A")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    input_file = browser.find_element(By.CSS_SELECTOR, "[name=\"file\"]")
    input_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
