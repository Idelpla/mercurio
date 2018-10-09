from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserModelTest(TestCase):

    def test_str(self):
        user = User(first_name='Ted', last_name='Mosby')
        self.assertEqual('Mosby Ted', user.__str__())
