from django.urls import path
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movies_list'),
    path('<int:pk>/', MovieDetailsAV.as_view(), name='movies_details'),
]
