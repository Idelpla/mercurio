# Generated by Django 2.1.2 on 2018-10-11 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statements', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
