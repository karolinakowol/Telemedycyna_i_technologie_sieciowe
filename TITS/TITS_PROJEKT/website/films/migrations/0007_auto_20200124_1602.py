# Generated by Django 2.2.7 on 2020-01-24 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_series_series_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='series_owner',
            new_name='owner',
        ),
    ]
