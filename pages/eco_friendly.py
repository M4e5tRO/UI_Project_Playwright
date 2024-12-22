import random
import allure
from playwright.sync_api import expect

from ..pages.base_page import BasePage
from ..pages.locators import eco_friendly_locators as loc
from ..test_data import data_list as dl


def paging_names(func):

    def wrapper(self):
        items_before = self.find_all(loc.item_name_loc)
        items_before_names = [item.inner_text() for item in items_before]

        func(self)

        items_after = self.find_all(loc.item_name_loc)
        items_after_names = [price.inner_text() for price in items_after]
        assert items_before_names != items_after_names, (
            f'Items before: {items_before_names}, Items after: {items_after_names}'
        )

    return wrapper


class EcoFriendly(BasePage):
    PAGE_URL = '/collections/eco-friendly.html'

    def check_sort_by_name(self, order="asc"):
        with allure.step(f'Check sorting by Product Name in {order.upper()} order'):
            items = self.find_all(loc.item_name_loc)
            values = [item.get_attribute("alt") for item in items]
            python_sorted = sorted(values, reverse=(order == "desc"))
            assert values == python_sorted, f'Expected: {python_sorted}, Actual: {values}'

    def check_sort_by_price(self, order="asc"):
        with allure.step(f'Check sorting by Price in {order.upper()} order'):
            items = self.find_all(loc.item_price_loc)
            values = [item.inner_text() for item in items]
            python_sorted = sorted(values, reverse=(order == "desc"))
            assert values == python_sorted, f'Expected: {python_sorted}, Actual: {values}'

    @allure.step('Check paging: Next')
    @paging_names
    def check_paging_next(self):
        self.find(loc.paging_next_loc).click()

    @allure.step('Check paging: Previous')
    @paging_names
    def check_paging_prev(self):
        self.find(loc.paging_prev_loc).click()

    @allure.step('Check paging: Random Item')
    @paging_names
    def check_paging_item(self):
        items = self.find_all(loc.paging_item_loc)
        item = random.choice(items)
        item.click()

    @allure.step('Check limiter')
    def check_limiter(self, limiter):
        self.page.select_option(loc.limiter_loc, value=limiter)
        self.page.dispatch_event(loc.limiter_loc, "change")
        expected_url = dl.limiter_urls.get(limiter)
        self.page.wait_for_url(expected_url)
        expect(self.page).to_have_url(expected_url)
