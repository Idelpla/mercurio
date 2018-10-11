from django.test import TestCase
from ..models import Account, Item


class AccountModelTest(TestCase):

    def test_str(self):
        account = Account(name='SAE')
        self.assertEqual('SAE', account.__str__())


class ItemModelTest(TestCase):

    def test_str(self):
        item = Item(account=Account(name='SAE'), name='first item')
        self.assertEqual('first item', item.__str__())
