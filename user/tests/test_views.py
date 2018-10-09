from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoggedInTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Ted',
                                                         password='a-super-secret-password',
                                                         first_name='Ted',
                                                         last_name='Mosby',)
        self.client.login(username='Ted', password='a-super-secret-password')


class LoginTest(TestCase):

    def test_uses_proper_template(self):
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'standard_form.html')

    def test_get_context_data(self):
        response = self.client.get(reverse('users:login'))
        self.assertIsNotNone(response.context['title'])


class DashboardTest(LoggedInTestCase):

    def test_uses_proper_template(self):
        response = self.client.get(reverse('users:dashboard'))
        self.assertTemplateUsed(response, 'user/dashboard.html')


class ElectronicAddress(LoggedInTestCase):

    def test_get_object(self):
        response = self.client.get(reverse('users:electronic_address'))
        self.assertEquals(response.context['object'], self.user)

    def test_uses_proper_template(self):
        response = self.client.get(reverse('users:electronic_address'))
        self.assertTemplateUsed(response, 'standard_form.html')

    def test_success_url(self):
        response = self.client.post(reverse('users:electronic_address'))
        self.assertRedirects(response, reverse('users:dashboard'))
