from playwright.sync_api import expect
import allure

from ..pages.base_page import BasePage
from ..pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    PAGE_URL = '/customer/account/create/'

    @allure.step('Fill in the form')
    def fill_in_form(self, first_name, last_name, email, password, conf_password):

        self.find(loc.first_name_loc).fill(first_name)
        self.find(loc.last_name_loc).fill(last_name)
        self.find(loc.email_loc).fill(email)
        self.find(loc.password_loc).fill(password)
        self.find(loc.conf_password_loc).fill(conf_password)

        self.find(loc.create_btn_loc).click()

    @allure.step('Check redirection page URL')
    def check_redirection_page_url(self, account_url):
        expect(self.page).to_have_url(account_url)

    @allure.step('Check success message')
    def check_success_message(self, message):
        page_message = self.find(loc.success_message_loc)

        expect(page_message).to_have_text(message)

    @allure.step('Check contact info')
    def check_contact_info(self, first_name, last_name, email):
        full_name = f'{first_name} {last_name}'

        contact_info = self.find(loc.contact_info_loc)
        contact_text = contact_info.inner_text().split("\n")
        full_name_text = contact_text[0]
        email_text = contact_text[1]

        assert full_name == full_name_text, f'Expected result: {full_name}, Actual result: {full_name_text}'
        assert email == email_text, f'Expected result: {email}, Actual result: {email_text}'

    @allure.step('Check inline error for required fields')
    def check_inline_error_for_required_fields(self, inline_error):
        self.find(loc.create_btn_loc).click()

        first_name_error = self.find(loc.first_name_error_loc)
        last_name_error = self.find(loc.last_name_error_loc)
        password_error = self.find(loc.password_error_loc)
        conf_password_error = self.find(loc.conf_password_error_loc)

        expect(first_name_error).to_have_text(inline_error)
        expect(last_name_error).to_have_text(inline_error)
        expect(password_error).to_have_text(inline_error)
        expect(conf_password_error).to_have_text(inline_error)

    @allure.step('Check password errors')
    def check_password_errors(self, invalid_pass_length, pass_error):
        self.find(loc.password_loc).fill(invalid_pass_length)
        self.find(loc.create_btn_loc).click()

        password_error = self.find(loc.password_error_loc)

        expect(password_error).to_have_text(pass_error)
