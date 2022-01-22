from django.urls import path
from watchlist_app.api.views import (WatchListAV, WatchllistDetailsAV, StreamPlatformAV, 
                                     StreamPlatformDetailsAV, ReviewList, ReviewDetail)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movies_list'),
    path('<int:pk>/', WatchllistDetailsAV.as_view(), name='movies_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='stream_details'),
    
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
    
    # path('stream/<int:pk>/review/', StreamPlatformDetailsAV.as_view(), name='stream_details'),
    # path('stream/review/<int:pk>/', ReviewDetail.as_view( ), name='review-details'),
]
