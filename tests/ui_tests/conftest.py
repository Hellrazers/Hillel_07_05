import pytest
from playwright.sync_api import Page, expect, Browser, APIRequestContext

from ui_models.base_page import BasePage


@pytest.fixture
def login_ui(page: Page) -> Page:
    page.goto("/")
    # page2 = page.context.new_page()
    # page2.goto("https://seleniumbase.io/w3schools/iframes")
    page.get_by_role("button", name="Sign In").click()
    page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.locator("app-signin-modal")).to_contain_text("Login")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')
    expect(page.locator('//div[@class="alert alert-success"]')).to_have_text('You have been successfully logged in')
    yield page



@pytest.fixture
def auth_login(browser_context_args, browser: Browser, api, ui_test_fixture) -> Page:
    token_api = api.api.token
    context = browser.new_context(
        **browser_context_args,
        storage_state={
            'cookies': [
                {
                    'name': 'sid',
                    'value': token_api,
                    'domain': '.forstudy.space',
                    'path': '/',
                }
            ]
        }
    )
    page  = context.new_page()
    base_page = BasePage(page)
    base_page.open()
    expect(base_page.alert_danger_locator).not_to_be_visible()
    # expect(page.locator('#userNavDropdown')).to_have_text('My profile')
    yield page

    page.close()
    context.close()


@pytest.fixture
def auth_login_pl(browser_context_args, browser: Browser, api_pl: APIRequestContext) -> Page:
    context = browser.new_context(
        **browser_context_args,
        storage_state=api_pl.storage_state()
    )
    page = context.new_page()
    base_page = BasePage(page)
    base_page.open()
    expect(base_page.alert_danger_locator).not_to_be_visible()
    # expect(page.locator('#userNavDropdown')).to_have_text('My profile')
    yield page

    page.close()
    context.close()