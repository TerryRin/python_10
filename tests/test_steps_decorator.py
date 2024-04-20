#Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
# 3. Шаги с декоратором @allure.step
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

def test_steps():
    with allure.step("Открыть страницу GitHub в браузере"):
        browser.open("https://github.com")

    with allure.step("Поиск репозитория"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переход по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переход на вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("Поиск Issues с нужным номером"):
        s(by.partial_text("#87")).should(be.visible)