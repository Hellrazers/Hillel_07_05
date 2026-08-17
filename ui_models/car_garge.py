from playwright.sync_api import Page

from ui_models.base_page import BasePage


class CarGaragePage(BasePage):
    PATH = '/panel/garage'


    def __init__(self, page: Page):
        super().__init__(page)
        self.brand_drop_down = page.locator('#addCarBrand')
        self.button_add_car = self.button_open_modal
        self.brand_drop_down_value = page.locator('select[id="addCarBrand"] option')
        self.car_model_drop_down = page.locator('#addCarModel')
        self.car_mileage_input = page.locator('#addCarMileage')
        self.car_button_add_car = self.button_in_modal_click_add



