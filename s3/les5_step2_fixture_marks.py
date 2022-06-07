import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    #pytest -s -v -m "not smoke" test.py Для запуска всех тестов, не отмеченных как smoke
    #pytest -s -v -m "smoke or regression" test.py Запустим smoke и regression-тесты
    #pytest -s -v -m "smoke and win10" test.py запустить только smoke-тесты для Windows 10
    #pytest -s -v -m smoke test.py запускает тесты с маркером smoke
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    @pytest.mark.skip(reason="Reason to skip test") # pytest -rsx Запускает тесты, пропускает отмеченные и выдает текст.
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
