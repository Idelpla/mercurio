from .models import Statement, Attachment
from django import forms
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class StatementForm(forms.ModelForm):
    class Media:
        js = ('js/jquery.formset.b4.js',)

    class Meta:
        model = Statement
        fields = (
            'year',
            'fiscal_position',
            'activity',
        )

    def __init__(self, *args, **kwargs):
        super(StatementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout()

        for key in self.fields.keys():
            self.helper.layout.fields.append(Field(key))


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = (
            'attachment',
        )


AttachmentFormSet = inlineformset_factory(Statement, Attachment, form=AttachmentForm, extra=1)


class AttachmentFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AttachmentFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.disable_csrf = True
        self.template = 'bootstrap4/table_inline_formset.html'
