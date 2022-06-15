from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

#Если вы запустить тесты без параметра (pytest -s -v test_parser.py), то ошибка
#Нужно указать значение параметра --browser_name=chrome (или firefox)
