from django.contrib import admin
from watchlist_app.models import Watchlist

@admin.register(Watchlist)
class WatchllistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','active']