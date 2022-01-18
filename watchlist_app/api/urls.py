from django.urls import path
from watchlist_app.api.views import movies_list, movies_details

urlpatterns = [
    path('list/', movies_list,name='movies_list'),
    path('<int:pk>/',movies_details, name='movies_details'),
]
