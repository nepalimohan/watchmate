from django.contrib import admin
from watchlist_app.models import Watchlist, StreamPlatform, Reviews

@admin.register(Watchlist)
class WatchllistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'storyline', 'platform','active', 'created']
    
@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website']
    
@admin.register(Reviews)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'description','watchlist','active','created','update']

# admin.site.register(Watchlist)
# admin.site.register(StreamPlatform)