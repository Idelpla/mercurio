from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def test_user_can_login(self):
        # Carlos goes to the site and after a few seconds is asked to login
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Carlos enters his username and password and is redirected to the root
        self.browser.find_element_by_name('email').send_keys('carlos@mercurio.com')
        self.browser.find_element_by_name('password').send_keys('qwerty12')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn(
            'Login',
            self.browser.find_element_by_tag_name('body').text
        ))
