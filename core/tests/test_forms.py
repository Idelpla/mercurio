from django.test import TestCase
from ..forms import ModelFormBase
from crispy_forms.helper import FormHelper

from account.models import Account

# TODO How to use a mock to avoid import of another app?
class DummyForm(ModelFormBase):
    class Meta:
        model = Account
        fields = ('name',)


class ModelFormBaseTest(TestCase):

    def test_init(self):
        form = DummyForm()
        self.assertIsInstance(form.helper, FormHelper)
