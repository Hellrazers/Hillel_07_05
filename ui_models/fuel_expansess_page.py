from playwright.sync_api import Page

from ui_models.base_page import BasePage


class FuelExpansessPage(BasePage):
    PATH = '/panel/expenses'



    def __init__(self, page: Page):
        super().__init__(page)
        self.drop_vechire_in_modal = page.locator('#addExpenseCar')
        self.input_mileage_in_modal = page.locator('#addExpenseMileage')
        self.input_number_of_liters_in_modal = page.locator('#addExpenseLiters')
        self.input_total_cost_in_modal = page.locator('#addExpenseTotalCost')



    def option_vechire_in_modal(self, item_id):
        self.page.locator(f'//option[contains(@value, "{item_id}")]')