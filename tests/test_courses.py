from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    # Проверит соответствие текста "Courses"
    expect(courses_title).to_have_text("Courses")

    courses_list_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    # Проверит соответствие текста "There is no results"
    expect(courses_list_empty_title).to_have_text("There is no results")

    courses_list_icon = page.get_by_test_id('courses-list-empty-view-icon')
    # Проверит видимость иконки
    expect(courses_list_icon).to_be_visible()

    courses_list_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    # Проверит соответствие описания пустого списка
    expect(courses_list_empty_description).to_have_text(
        "Results from the load test pipeline will be displayed here")