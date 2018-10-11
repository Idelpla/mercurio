from django.db import models
from django.utils.translation import gettext as _

from tax.models import FiscalPosition, Activity
from user.models import User


class Statement(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation_date'), auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name=_('owner'),  on_delete=models.CASCADE, related_name='statements')
    year = models.SmallIntegerField(verbose_name=_('year'))
    fiscal_position = models.ForeignKey(FiscalPosition, verbose_name=_('fiscal position'), on_delete=models.PROTECT, related_name='+')
    activity = models.ForeignKey(Activity, verbose_name=_('activity'), on_delete=models.PROTECT, related_name='+')
