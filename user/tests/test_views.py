from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('users:login'))
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.context['title'])


class DashboardTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_get(self):
        response = self.client.get(reverse('users:dashboard'))
        self.assertEquals(response.status_code, 200)


class ElectronicAddressTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_get(self):
        response = self.client.get(reverse('users:electronic_address'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['object'], self.user)
