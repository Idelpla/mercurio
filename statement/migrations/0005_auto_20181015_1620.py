# Generated by Django 2.1.2 on 2018-10-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0004_auto_20181014_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to='attachments', verbose_name='attachment'),
        ),
    ]