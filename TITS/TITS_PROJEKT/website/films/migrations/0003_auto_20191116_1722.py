# Generated by Django 2.2.7 on 2019-11-16 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20191116_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='film_director',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_title',
            new_name='title',
        ),
    ]
