from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    electronic_address = models.EmailField(verbose_name=_('electronic address'), max_length=255, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
