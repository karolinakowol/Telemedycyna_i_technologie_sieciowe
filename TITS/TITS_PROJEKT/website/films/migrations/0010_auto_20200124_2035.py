# Generated by Django 2.2.7 on 2020-01-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_auto_20200124_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='film_played',
        ),
        migrations.AddField(
            model_name='actors',
            name='film_played',
            field=models.ManyToManyField(to='films.Film'),
        ),
        migrations.RemoveField(
            model_name='actors',
            name='series_played',
        ),
        migrations.AddField(
            model_name='actors',
            name='series_played',
            field=models.ManyToManyField(to='films.Series'),
        ),
    ]
