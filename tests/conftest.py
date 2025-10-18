import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнит поле "Email" значением "milada.savitskaya@gmail.com"
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("milada.savitskaya@gmail.com")
    # Заполнит поле "Username" значением "milada"
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("milada")
    # Заполнит поле "Password" значением "milada"
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("milada")

    # Клик на кнопку регистрации
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    yield page