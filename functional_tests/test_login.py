from .base import FunctionalTest
from django.contrib.auth import get_user_model


class LoginTest(FunctionalTest):

    def setUp(self):
        get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        return super(LoginTest, self).setUp()

    def test_registered_user_can_login(self):

        # Ted goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Ted enters his username and password and is redirected to his dashboard
        self.browser.find_element_by_name('username').send_keys('Ted')
        self.browser.find_element_by_name('password').send_keys('a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn(
            'Dashboard',
            self.browser.find_element_by_tag_name('body').text
        ))

    def test_registered_user_types_wrong_password_cant_login(self):

        # Ted goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Ted enters his username but types a wrong password and so he is not redirected to his dashboard
        self.browser.find_element_by_name('username').send_keys('Ted')
        self.browser.find_element_by_name('password').send_keys('not-a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))

    def test_not_registered_user_cant_login(self):
        # Barney goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Barney enters a username and password but, as he is not registered, he is not redirected to the dashboard
        self.browser.find_element_by_name('username').send_keys('Barney')
        self.browser.find_element_by_name('password').send_keys('a-super-secret-password')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))
