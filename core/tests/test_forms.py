from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import ModelFormBase

User = get_user_model()


class DummyForm(ModelFormBase):
    class Meta:
        model = User
        fields = ('username', 'email',)


class ModelFormBaseTest(TestCase):

    def test_init(self):
        form = DummyForm()
        self.assertIsInstance(form.helper, FormHelper)
