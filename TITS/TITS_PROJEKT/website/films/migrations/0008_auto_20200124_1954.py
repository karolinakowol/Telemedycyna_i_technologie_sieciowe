# Generated by Django 2.2.7 on 2020-01-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20200124_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='actors',
            name='actor_photo',
            field=models.CharField(max_length=100000000, null=True),
        ),
    ]
