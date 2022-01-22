from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV, WatchllistDetailsAV, 
                                    ReviewList, ReviewCreate, 
                                    ReviewDetail, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movies_list'),
    path('<int:pk>/', WatchllistDetailsAV.as_view(), name='movies_details'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='stream_details'),
    
    path('', include(router.urls)),  #using routers instead of views to replace two urls  
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create/'), #these are important links
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),  #to understand
    path('stream/review/<int:pk>/', ReviewDetail.as_view( ), name='review-details'),
]
