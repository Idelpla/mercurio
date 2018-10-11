from django.contrib.auth import get_user_model

from .base import FunctionalTest


class ProviderTest(FunctionalTest):
    def setUp(self):
        get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        return super(ProviderTest, self).setUp()

    def test_setting_electronic_address(self):
        self.login('Ted', 'a-super-secret-password', 'users:dashboard')

        # Ted notices a link asking him for his electronic address, so he clicks it and is redirected to a page where
        # there is an input box to fill in an email.
        self.browser.find_element_by_link_text('Electronic Address').click()
        self.wait_for(lambda: self.assertIsNotNone(self.browser.find_element_by_name('electronic_address').text))

        # He types his email, submits and is redirected to the dashboard
        self.browser.find_element_by_name('electronic_address').send_keys('ted@myemai.com')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))

        # He sees his electronic address in the Dashboard
        self.assertIn('ted@myemai.com', self.browser.find_element_by_tag_name('body').text)

        # Ted notices an error in his electronic address, so he clicks the link again and corrects it.
        self.browser.find_element_by_link_text('Electronic Address').click()
        self.wait_for(lambda: self.assertIsNotNone(self.browser.find_element_by_name('electronic_address').text))

        # He types his email, submits and is redirected to the dashboard
        self.browser.find_element_by_name('electronic_address').clear()
        self.browser.find_element_by_name('electronic_address').send_keys('ted@myemail.com')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))

        # He sees his correct electronic address in the Dashboard
        self.assertIn('ted@myemail.com', self.browser.find_element_by_tag_name('body').text)

    def test_listing_statements(self):
        self.login('Ted', 'a-super-secret-password', 'users:dashboard')

        # Ted notices a link to see his statements as provider. He want to take a look so he clicks it and is redirected
        # to a new page.
        self.browser.find_element_by_link_text('Statements').click()
        self.wait_for(lambda: self.assertIn('Your Statements', self.browser.find_element_by_tag_name('body').text))
