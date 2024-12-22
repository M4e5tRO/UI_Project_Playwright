import allure

from ..test_data import data_list as dl


@allure.feature('Eco Friendly')
class TestEcoFriendly:

    @allure.story('Test Sorting By Product Name')
    def test_sort_by_name(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.sort_by(dl.sort_by_product_name_value)
        eco_friendly.switch_desc()
        eco_friendly.check_sort_by_name(order='desc')
        eco_friendly.switch_asc()
        eco_friendly.check_sort_by_name(order='asc')

    @allure.story('Test Sorting By Price')
    def test_sort_by_price(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.sort_by(dl.sort_by_price_value)
        eco_friendly.switch_desc()
        eco_friendly.check_sort_by_price(order="desc")
        eco_friendly.switch_asc()
        eco_friendly.check_sort_by_price(order="asc")

    @allure.story('Test Paging')
    def test_paging(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.check_paging_next()
        eco_friendly.check_paging_prev()
        eco_friendly.check_paging_item()

    @allure.story('Test Limiter')
    def test_limiter(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.check_limiter(dl.limiter_24)
        eco_friendly.check_limiter(dl.limiter_36)
        eco_friendly.check_limiter(dl.limiter_12)
