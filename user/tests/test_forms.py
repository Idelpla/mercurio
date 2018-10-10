from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import ElectronicAddressForm

User = get_user_model()


class ElectronicAddressFormTest(TestCase):

    def test_init(self):
        form = ElectronicAddressForm()
        self.assertIsInstance(form.helper, FormHelper)
