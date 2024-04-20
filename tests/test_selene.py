#Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
# 1. Чистый Selene (без шагов)
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#87")).should(be.visible)
