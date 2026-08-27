import os
import random
import time

import pytest
from playwright.sync_api import Page, expect

from ui_models.base_page import BasePage
from ui_models.car_garge import CarGaragePage
from ui_models.fuel_expansess_page import FuelExpansessPage
from ui_models.login_page import LoginPage

@pytest.mark.ui_test
def test_login_no_pom(page: Page) -> None:
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

@pytest.mark.ui_test
@pytest.mark.parametrize('email, password, status', [
    (os.getenv('USER_LOGIN'), os.getenv('USER_PASSWORD'), 'success'), # 1 run -success
    # ('asda@gmail.com', os.getenv('USER_PASSWORD'), 'failed')
]) #2 run - failed
def test_2(page: Page, email, password, status) -> None:
    login_page = LoginPage(page)
    login_page.open()
    car_garage = login_page.login(email, password)
    if status == 'success':
        expect(login_page.alert_success_locator).to_have_text('You have been successfully logged in')
    elif status == 'failed':
        expect(login_page.alert_danger_locator).to_have_text('Wrong email or password')
    car_garage.button_add_car.click()
    time.sleep(5)

@pytest.mark.api_test
@pytest.mark.ui_test
def test_create_car(auth_login, delete_car_api):
    CAR_MILEAGE  = '123'
    car_page = CarGaragePage(auth_login)
    car_page.open()
    car_page.button_add_car.click()
    expect(car_page.modal_title).to_have_text('Add a car')
    expect(car_page.brand_drop_down_value).to_have_text(["Audi", "BMW", "Ford", "Porsche","Fiat"])
    car_page.brand_drop_down.select_option('Ford')
    car_page.car_model_drop_down.select_option('Fusion')
    car_page.car_mileage_input.fill(CAR_MILEAGE)
    with auth_login.expect_response("**/api/cars") as response_info:
        car_page.car_button_add_car.click()
        print(response_info)
    resp_car_id = response_info.value.json()['data']['id']
    delete_car_api.append(resp_car_id)
    expect(car_page.alert_success_locator).to_have_text('Car added1111')


@pytest.mark.ui_test
def test_create_car_pl_login(auth_login_pl, delete_car_api):

    CAR_MILEAGE  = '123'
    car_page = CarGaragePage(auth_login_pl)
    car_page.open()
    car_page.button_add_car.click()
    expect(car_page.modal_title).to_have_text('Add a car')
    expect(car_page.brand_drop_down_value).to_have_text(["Audi", "BMW", "Ford", "Porsche","Fiat"])
    car_page.brand_drop_down.select_option('Ford')
    car_page.car_model_drop_down.select_option('Fusion')
    car_page.car_mileage_input.fill(CAR_MILEAGE)
    with auth_login_pl.expect_response("**/api/cars") as response_info:
        car_page.car_button_add_car.click()
        print(response_info)
    resp_car_id = response_info.value.json()['data']['id']
    delete_car_api.append(resp_car_id)
    expect(car_page.alert_success_locator).to_have_text('Car added')

@pytest.mark.ui_test
def test_create_expensess(auth_login: Page):
    NUMBER_OF_LIST = '5'
    TOTAL_COST = '4'
    expenses_page = FuelExpansessPage(auth_login)
    expenses_page.open()
    with auth_login.expect_response(lambda resp:
                                    resp.url == f'{os.getenv("basic_url")}/api/cars'
                                    and resp.status == 200
                                    ) as response_info:
        expenses_page.button_open_modal.click()
        response_get_car = response_info.value.json().get('data')
    expect(expenses_page.modal_title).to_have_text('Add an expense')
    value = random.choice(range(0, len(response_get_car)))
    MIELGE = int(response_get_car[value]['mileage']) + 1
    expenses_page.drop_vechire_in_modal.select_option(index=value)
    expenses_page.input_mileage_in_modal.click()
    expenses_page.input_mileage_in_modal.press("ArrowUp")
    expenses_page.input_number_of_liters_in_modal.fill(NUMBER_OF_LIST)
    expenses_page.input_total_cost_in_modal.fill(TOTAL_COST)

    with auth_login.expect_response("**/api/expenses") as response_info:

        expenses_page.button_in_modal_click_add.click()
        print(response_info.value.json())

