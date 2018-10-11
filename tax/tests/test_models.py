from django.test import TestCase
from ..models import FiscalPosition, Activity


class FiscalPositionModelTest(TestCase):

    def test_str(self):
        position = FiscalPosition(name='Exempt')
        self.assertEqual('Exempt', position.__str__())


class ActivityModelTest(TestCase):

    def test_str(self):
        activity = Activity(name='It Services')
        self.assertEqual('It Services', activity.__str__())
