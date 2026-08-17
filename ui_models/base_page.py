from playwright.sync_api import Page


class BasePage:
    PATH = '/'

    def __init__(self, page:Page):
        self.page = page
        self.alert_danger_locator = page.locator('[class="alert alert-danger"]')
        self.alert_success_locator = page.locator('div[class="alert alert-success"]')
        self.button_open_modal = page.locator('button[class="btn btn-primary"]')
        self.modal_title = page.locator('//div[@class="modal-content"]//h4')
        self.button_in_modal_click_add = page.locator('[class="modal-footer d-flex justify-content-end"] button[class="btn btn-primary"]')
    def open(self):
        return self.page.goto(self.PATH)


