from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.decorators import  login_required

app_name = 'films'

urlpatterns = [
    # /films/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # films/register

    # /films/<film_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^add/$', login_required(views.FilmCreate.as_view()), name='film-add'),

    url(r'^(?P<pk>[0-9]+)/update/$', login_required(views.FilmUpdate.as_view()), name='film-update'),

    # url(r'^(?P<pk>[0-9]+)/delete/$', views.FilmDelete.as_view(), name='film-delete'),

    url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.FilmDelete.as_view()), name='film-delete'),

    url('r^signup/$', views.SignUp.as_view(), name='signup'),

    path('signup/', views.SignUp.as_view(), name='signup'),

    # /films/series/
    url(r'^series/$', views.SeriesIndexView.as_view(), name='series-index'),

    # /films/series/detail
    url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesDetailView.as_view(), name='series-detail'),
    # /films/series/add
    url(r'^series/add/$', login_required(views.SeriesCreate.as_view()), name='series-add'),
    # /films/series/pk/update/
    url(r'^series/(?P<pk>[0-9]+)/update/$', login_required(views.SeriesUpdate.as_view()), name='series-update'),
    # /films/series/1/delete/
    url(r'^series/(?P<pk>[0-9]+)/delete/$', login_required(views.SeriesDelete.as_view()), name='film-delete'),
]
