from django.contrib.auth import get_user_model
from django.urls import reverse

from tax.models import FiscalPosition, Activity
from statement.models import Statement
from .base import FunctionalTest

from selenium.webdriver.support.ui import Select
from random import randint

User = get_user_model()


class ProviderTest(FunctionalTest):
    def setUp(self):
        # Dummy objects
        fiscal_positions = list()
        activities = list()
        for i in range(5):
            fiscal_positions.append(FiscalPosition.objects.create(name='Fiscal Position ' + str(i + 1)))
            activities.append(Activity.objects.create(name='Activity ' + str(i + 1)))

        for u in range(3):
            user = User.objects.create_user(username='Dummy ' + str(u + 1), password='a-dummy-password')

            for i in range(10):
                Statement.objects.create(year=2018,
                                         fiscal_position=fiscal_positions[randint(0, 4)],
                                         activity=activities[randint(0, 4)],
                                         owner=user)

        User.objects.create_user(username='Ted', password='a-super-secret-password')
        return super(ProviderTest, self).setUp()

    def test_electronic_address(self):
        self.login('Ted', 'a-super-secret-password', 'users:dashboard')

        # Ted notices a link asking him for his electronic address, so he clicks it and is redirected to a page where
        # there is an input box to fill in an email.
        self.browser.find_element_by_link_text('Electronic Address').click()
        self.wait_for(lambda: self.assertIn(reverse('users:electronic_address'), self.browser.current_url))

        # He types his email, submits and is redirected to the dashboard
        self.browser.find_element_by_name('electronic_address').send_keys('ted@myemai.com')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))

        # He sees his electronic address in the Dashboard
        self.assertIn('ted@myemai.com', self.browser.find_element_by_tag_name('body').text)

        # Ted notices an error in his electronic address, so he clicks the link again and corrects it.
        self.browser.find_element_by_link_text('Electronic Address').click()
        self.wait_for(lambda: self.assertIn(reverse('users:electronic_address'), self.browser.current_url))

        # He types his email, submits and is redirected to the dashboard
        self.browser.find_element_by_name('electronic_address').clear()
        self.browser.find_element_by_name('electronic_address').send_keys('ted@myemail.com')
        self.browser.find_element_by_class_name('btn').click()
        self.wait_for(lambda: self.assertIn('Dashboard', self.browser.find_element_by_tag_name('body').text))

        # He sees his correct electronic address in the Dashboard
        self.assertIn('ted@myemail.com', self.browser.find_element_by_tag_name('body').text)

    def test_new_statement(self):
        self.login('Ted', 'a-super-secret-password', 'users:dashboard')

        # Ted notices a link to see his statements as provider. He want to take a look so he clicks it and is redirected
        # to a new page.
        self.browser.find_element_by_link_text('Statements').click()
        self.wait_for(lambda: self.assertIn(reverse('statements:list'), self.browser.current_url))

        # Ted sees he has no statements so he decides to create one.
        self.wait_for(lambda: self.assertIn('No statements found.', self.browser.find_element_by_tag_name('body').text))
        self.browser.find_element_by_link_text('New Statement').click()
        self.wait_for(lambda: self.assertIn(reverse('statements:new'), self.browser.current_url))

        self.browser.find_element_by_name('year').send_keys('2018')
        Select(self.browser.find_element_by_name('fiscal_position')).select_by_visible_text('Fiscal Position 1')
        Select(self.browser.find_element_by_name('activity')).select_by_visible_text('Activity 1')
        self.browser.find_element_by_class_name('btn').click()

        # Ted is redirected to a page where he can see the detail of his statement
        teds_statement = Statement.objects.last()
        self.wait_for(lambda: self.assertIn(reverse('statements:detail', kwargs={'pk': teds_statement.pk}), self.browser.current_url))
        self.assertIn('Statement object ({})'.format(teds_statement.pk), self.browser.find_element_by_tag_name('body').text)

    def test_cant_see_other_owner_statement(self):
        other_user_statement = Statement.objects.filter(owner__username='Dummy 2').first()

        self.login('Dummy 1', 'a-dummy-password', 'statements:list')

        self.browser.get(self.live_server_url + reverse('statements:detail', kwargs={'pk': other_user_statement.pk}))
        self.wait_for(lambda: self.assertIn(reverse('statements:detail', kwargs={'pk': other_user_statement.pk}), self.browser.current_url))
        self.assertIn('Statement object ({})'.format(other_user_statement.pk), self.browser.find_element_by_tag_name('body').text)
        self.fail('Write expected message.')

