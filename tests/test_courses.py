from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
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


def test_create_course(courses_list_page:CoursesListPage, create_course_page:CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(title='', description='', estimated_time='',max_score='0',min_score='0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(title='Playwrigh', description='Playwright', estimated_time='2 weeks',max_score='100',min_score='10')
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(index=0,title='Playwrigh', estimated_time='2 weeks',max_score='100',min_score='10')



