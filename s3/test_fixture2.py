import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class") #Фикстура, которая создает webdriver и возврашает его значение
def browser(): #scope="class" фикстура будет вызываться один раз для класса
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
# После завершения теста, который вызывал фикстуру, выполнение фикстуры
# продолжится со строки, следующей за строкой со словом yield:

# фикстуру нужно запустить для каждого теста даже без явного вызова
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
