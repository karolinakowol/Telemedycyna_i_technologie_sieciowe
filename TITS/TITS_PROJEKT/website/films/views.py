from .models import Film, Actors, Series
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    template_name = 'films/index.html'
    context_object_name = 'all_films'

    def get_queryset(self):
        return Film.objects.all()


class SeriesIndexView(generic.ListView):
    template_name = 'films/series_index.html'
    context_object_name = 'all_series'

    def get_queryset(self):
        return Series.objects.all()


class ActorsIndexView(generic.ListView):
    template_name = 'films/actors_index.html'
    context_object_name = 'all_actors'

    def get_queryset(self):
        return Actors.objects.all()


class DetailView(generic.DetailView):
    model = Film
    template_name = 'films/detail.html'


class SeriesDetailView(generic.DetailView):
    model = Series
    template_name = 'films/series_detail.html'


class ActorsDetailView(generic.DetailView):
    model = Actors
    template_name = 'films/actors_detail.html'


class FilmCreate(CreateView):
    model = Film
    fields = ['director', 'title', 'film_genre', 'film_logo']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FilmCreate, self).form_valid(form)


# Create Series
class SeriesCreate(CreateView):
    model = Series
    fields = ['series_director', 'series_title', 'series_genre', 'series_logo']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(SeriesCreate, self).form_valid(form)


class FilmUpdate(UpdateView):
    model = Film
    fields = ['director', 'title', 'film_genre', 'film_logo']


# Series Update
class SeriesUpdate(UpdateView):
    model = Series
    fields = ['series_director', 'series_title', 'series_genre', 'series_logo']


class FilmDelete(DeleteView):
    model = Film
    success_url = reverse_lazy('films:index')


# Series Delete
class SeriesDelete(DeleteView):
    model = Series
    success_url = reverse_lazy('films:series-index')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
