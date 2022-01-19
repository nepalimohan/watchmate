from django.contrib import admin
from watchlist_app.models import Watchlist, StreamPlatform

# @admin.register(Watchlist)
# class WatchllistModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'description','active']

admin.site.register(Watchlist)
admin.site.register(StreamPlatform)