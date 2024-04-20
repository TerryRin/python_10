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
def test_devorator_steps():
    open_github()
    search_repo()
    open_repo()
    open_issues()
    search_issues()

@allure.step("Открыть страницу GitHub в браузере")
def open_github():
    browser.open("https://github.com")


@allure.step("Поиск репозитория")
def search_repo():
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()


@allure.step("Переход по ссылке репозитория")
def open_repo():
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Переход на вкладку Issues")
def open_issues():
    s("#issues-tab").click()


@allure.step("Поиск Issues с нужным номером")
def search_issues():
    s(by.partial_text("#87")).should(be.visible)
