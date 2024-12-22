from playwright.sync_api import Page, Locator
import allure

from ..pages.locators import base_locators as loc
from ..test_data import data_list as dl


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    PAGE_URL = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        with allure.step(f'Open page: {self.BASE_URL}{self.PAGE_URL}'):
            if self.PAGE_URL:
                self.page.goto(f'{self.BASE_URL}{self.PAGE_URL}')
            else:
                raise NotImplementedError('Page can not be opened for this page class')

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Find elements by locator')
    def find_all(self, locator) -> list[Locator]:
        return self.page.locator(locator).all()

    def sort_by(self, sort_by_value):
        with allure.step(f'Sort by {sort_by_value}'):
            self.page.select_option(loc.sort_by_loc, value=sort_by_value)
            self.page.dispatch_event(loc.sort_by_loc, "change")
            expected_url = dl.sort_by_urls.get(sort_by_value)
            self.page.wait_for_url(expected_url)

    @allure.step('Switch in ASC order')
    def switch_asc(self):
        switch_asc = self.find(loc.switch_asc_loc)
        switch_asc.click()
        self.page.wait_for_load_state('load')

    @allure.step('Switch in DESC order')
    def switch_desc(self):
        switch_desc = self.find(loc.switch_desc_loc)
        switch_desc.click()
        self.page.wait_for_load_state('load')
