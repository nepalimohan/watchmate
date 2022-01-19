from django.contrib import admin
from watchlist_app.models import Watchlist, StreamPlatform

@admin.register(Watchlist)
class WatchllistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'storyline','active', 'created']
    
@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website']

# admin.site.register(Watchlist)
# admin.site.register(StreamPlatform)