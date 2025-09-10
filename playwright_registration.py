from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Заполнит поле "Email" значением "user.name@gmail.com"
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")
    #Заполнит поле "Username" значением "username"
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")
    #Заполнит поле "Password" значением "password"
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("Password")
    #Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    #Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard_title = page.locator('//div//h6[@data-testid="dashboard-toolbar-title-text"]')
    #Проверим видимость title
    expect(dashboard_title).to_be_visible()
    #Проверим соответствие текста "Dashboard"
    expect(dashboard_title).to_have_text("Dashboard")