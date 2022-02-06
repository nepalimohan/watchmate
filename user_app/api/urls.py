from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_app.api.views import registration_view, LogoutView

urlpatterns = [
    #Token Auth URLS
    # path('login/', obtain_auth_token, name='login'),
    # path('register/', RegistrationView.as_view(), name='register'),
    path('register/', registration_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    #JWT AUTH URLS
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]