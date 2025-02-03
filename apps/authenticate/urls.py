from django.urls import path
from .views import RegisterView ,endpoint
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',endpoint,name="home"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]