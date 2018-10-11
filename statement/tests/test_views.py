from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class StatementListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_url(self):
        response = self.client.get(reverse('statements:list'))
        self.assertEquals(response.status_code, 200)

    def test_get_queryset(self):
        self.fail('Write me')


class StatementNewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_url(self):
        response = self.client.get(reverse('statements:new'))
        self.assertEquals(response.status_code, 200)

    def test_form_valid(self):
        self.fail('Write me')
