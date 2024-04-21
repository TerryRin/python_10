# Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
# 2. Лямбда шаги через with allure.step
import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Поиск репозитория")
@allure.story("Лямбда шаги через with allure.step")
@allure.link("https://github.com", name="Test")

def test_decorator_steps():
    open_github()
    search_repo("eroshenkoam/allure-example")
    open_repo("eroshenkoam/allure-example")
    open_issues()
    search_issues_number("#87")

@allure.step("Открыть страницу GitHub в браузере")
def open_github():
    browser.open("https://github.com")

@allure.step(f"Поиск репозитория")
def search_repo(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()

@allure.step("Переход по ссылке репозитория")
def open_repo(repo):
    s(by.link_text(repo)).click()

@allure.step("Переход на вкладку Issues")
def open_issues():
    s("#issues-tab").click()

@allure.step("Поиск Issues с нужным номером")
def search_issues_number(number):
    s(by.partial_text(number)).should(be.visible)
