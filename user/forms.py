from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit


class LoginFormHelper(FormHelper):
    layout = Layout(
        Field('username'),
        Field('password'),
        Div(
            Submit('submit', 'Login'),
        )
    )
