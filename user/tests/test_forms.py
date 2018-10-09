from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import ElectronicAddressForm

User = get_user_model()


class ElectronicAddressFormTest(TestCase):

    def setUp(self):
        self.form = ElectronicAddressForm()

    def test_has_correct_model(self):
        self.assertEqual(self.form._meta.model, User)

    def test_has_correct_fields(self):
        self.assertIn('electronic_address', self.form.fields)

    def test_has_crispy_helper(self):
        self.assertIsInstance(self.form.helper, FormHelper)
