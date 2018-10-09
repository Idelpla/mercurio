from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginFormHelper(FormHelper):
    layout = Layout(
        Field('username'),
        Field('password'),
        Div(
            Submit('submit', 'Login'),
        )
    )


class ElectronicAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'electronic_address',
        )

    def __init__(self, *args, **kwargs):
        super(ElectronicAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()

        for key in self.fields.keys():
            self.helper.layout.fields.append(Field(key))

        self.helper.layout.fields.append(Div(Submit('submit', 'Submit'),))
