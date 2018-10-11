from django.db import models
from django.utils.translation import gettext as _


class FiscalPosition(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)

    def __str__(self):
        return self.name
