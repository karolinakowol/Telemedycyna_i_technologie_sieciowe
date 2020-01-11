from django.contrib import admin

from .models import Film, Actors, Series

admin.site.register(Film)
admin.site.register(Actors)
admin.site.register(Series)
