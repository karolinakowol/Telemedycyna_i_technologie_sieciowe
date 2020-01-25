from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Film(models.Model):
    director = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    film_genre = models.CharField(max_length=100)
    film_logo = models.CharField(max_length=100000000)
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('films:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'film ' + self.title + 'by' + self.director


class Series(models.Model):
    series_director = models.CharField(max_length=250)
    series_title = models.CharField(max_length=500)
    series_genre = models.CharField(max_length=100)
    series_logo = models.CharField(max_length=100000000)
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('films:series-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'series' + self.series_title + 'by' + self.series_director


class Actors(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=500)
    film_played = models.ManyToManyField(Film, null=True)
    series_played = models.ManyToManyField(Series, null=True)
    actor_photo = models.CharField(max_length=100000000, null=True)

    def __str__(self):
        return self.first_name
