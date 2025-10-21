import pytest

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page:RegistrationPage, dashboard_page:DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Заполняем форму регистрации
    registration_page.fill_registration_form(username="username",email="user.name@gmail.com", password="Password")
    # Клик по кнопке "Registration"
    registration_page.click_registration_button()
    # Проверка на странице Dashboard видимости заголовка и текста
    dashboard_page.check_visible_dashboard_title_and_text()