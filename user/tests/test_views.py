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

    def test_url(self):
        response = self.client.get(reverse('users:login'))
        self.assertEquals(response.status_code, 200)

    def test_get_context_data(self):
        response = self.client.get(reverse('users:login'))
        self.assertIsNotNone(response.context['title'])


class DashboardTest(LoggedInTestCase):

    def test_url(self):
        response = self.client.get(reverse('users:dashboard'))
        self.assertEquals(response.status_code, 200)


class ElectronicAddressTest(LoggedInTestCase):

    def test_url(self):
        response = self.client.get(reverse('users:electronic_address'))
        self.assertEquals(response.status_code, 200)

    def test_get_object(self):
        response = self.client.get(reverse('users:electronic_address'))
        self.assertEquals(response.context['object'], self.user)
