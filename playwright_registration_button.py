from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Проверит, что кнопка Login не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Заполнит поле "Email" значением "user.name@gmail.com"
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")
    #Заполнит поле "Username" значением "username"
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")
    #Заполнит поле "Password" значением "password"
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    #Проверит, что кнопка Login активна
    expect(registration_button).not_to_be_disabled()