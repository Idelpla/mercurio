from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit
from django.contrib.auth import get_user_model

from core.forms import ModelFormBase

User = get_user_model()


class LoginFormHelper(FormHelper):
    layout = Layout(
        Field('username'),
        Field('password'),
        Div(
            Submit('submit', 'Login'),
        )
    )


class ElectronicAddressForm(ModelFormBase):
    class Meta:
        model = User
        fields = (
            'electronic_address',
        )
