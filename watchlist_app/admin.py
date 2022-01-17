from django.contrib import admin
from watchlist_app.models import Movie

@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','active']