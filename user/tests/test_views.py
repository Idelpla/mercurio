from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoggedInTestCase(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')


class DashboardTest(LoggedInTestCase):

    def test_uses_dashboard_template(self):
        response = self.client.get(reverse('users:dashboard'))
        self.assertTemplateUsed(response, 'user/dashboard.html')


class LoginTest(TestCase):

    def test_uses_login_template(self):
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'standard_form.html')

    def test_get_context_data(self):
        response = self.client.get(reverse('users:login'))
        self.assertIsNotNone(response.context['title'])
        self.assertIsNotNone(response.context['form_helper'])
