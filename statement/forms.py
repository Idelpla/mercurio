from core.forms import ModelFormBase
from .models import Statement


class StatementForm(ModelFormBase):
    class Meta:
        model = Statement
        fields = (
            'year',
            'fiscal_position',
            'activity',
        )
