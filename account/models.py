from django.db import models
from django.utils.translation import gettext as _


class Account(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    account = models.ForeignKey(Account, verbose_name=_('account'), on_delete=models.CASCADE, related_name='items')
    name = models.CharField(verbose_name=_('name'), max_length=100)

    def __str__(self):
        return self.name
