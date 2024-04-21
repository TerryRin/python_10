#Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
# 4. Разметку тестов всеми аннотациями
import json
import allure
from allure_commons.types import Severity
from allure import attachment_type


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Поиск репозитория")
@allure.story("Лямбда шаги через with allure.step")
@allure.link("https://github.com", name="Test")

def test_attachments():
    # Текст
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    # HTML
    allure.attach("<h1>Test</h1>", name="Html", attachment_type=attachment_type.HTML)
    # JSON
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)
