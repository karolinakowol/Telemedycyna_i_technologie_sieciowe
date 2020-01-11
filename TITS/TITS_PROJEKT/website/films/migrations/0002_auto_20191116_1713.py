# Generated by Django 2.2.7 on 2019-11-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='director',
            new_name='film_director',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='title',
            new_name='film_title',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='director',
            new_name='series_director',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='title',
            new_name='series_title',
        ),
        migrations.AlterField(
            model_name='film',
            name='film_logo',
            field=models.CharField(max_length=100000000),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_logo',
            field=models.CharField(max_length=100000000),
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),
                ('film_played', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Film')),
                ('series_played', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Series')),
            ],
        ),
    ]
