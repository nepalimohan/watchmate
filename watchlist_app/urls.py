from django.urls import path
from watchlist_app.views import movies_list

urlpatterns = [
    path('list/', movies_list,name='movies_list'),
]
