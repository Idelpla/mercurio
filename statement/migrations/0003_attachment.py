# Generated by Django 2.1.2 on 2018-10-14 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0002_statement_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='', verbose_name='attachment')),
                ('statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='statement.Statement')),
            ],
        ),
    ]