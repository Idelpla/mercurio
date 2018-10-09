from .base import FunctionalTest
from django.contrib.auth import get_user_model


class LoginFailedTest(FunctionalTest):

    def test_registered_user_types_wrong_password_cant_login(self):

        # Ted goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn('login', self.browser.current_url))

        # Ted enters his username but types a wrong password and so he is not redirected to his dashboard
        self.browser.find_element_by_name('username').send_keys('Ted')
        self.browser.find_element_by_name('password').send_keys('not-a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('login', self.browser.current_url))

    def test_not_registered_user_cant_login(self):
        # Barney goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn('login', self.browser.current_url))

        # Barney enters a username and password but, as he is not registered, he is not redirected to the dashboard
        self.browser.find_element_by_name('username').send_keys('Barney')
        self.browser.find_element_by_name('password').send_keys('a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('login', self.browser.current_url))


class UserSetsElectronicAddress(FunctionalTest):
    def setUp(self):
        get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        return super(UserSetsElectronicAddress, self).setUp()

    def test_user_can_set_electronic_address(self):

        # Ted goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn('login', self.browser.current_url))

        # Ted enters his username and password and is redirected to his dashboard
        self.browser.find_element_by_name('username').send_keys('Ted')
        self.browser.find_element_by_name('password').send_keys('a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))

        # Ted notices a link asking him for his electronic address, so he clicks it and is redirected to a page where
        # there is an inputbox to fill in an email.
        self.browser.find_element_by_link_text('here').click()
        self.wait_for(lambda: self.assertIsNotNone(self.browser.find_element_by_name('electronic_address').text))

        # He types his email, submits and is redirected to the dashboard
        self.browser.find_element_by_name('electronic_address').send_keys('ted@myemail.com')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))
