from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field
from django import forms


class ModelFormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelFormBase, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout()

        for key in self.fields.keys():
            self.helper.layout.fields.append(Field(key))

        self.helper.layout.fields.append(HTML(r"{% include '_includes/_standard_form_buttons.html' %}"))
