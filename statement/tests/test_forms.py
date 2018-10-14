from django.test import TestCase
from ..forms import StatementForm
from crispy_forms.helper import FormHelper


class StatementFormTest(TestCase):

    def test_init(self):
        form = StatementForm()
        self.assertIsInstance(form.helper, FormHelper)
        self.assertIs(form.helper.form_tag, False)
        self.assertIs(len(form.helper.layout.fields), 3)
