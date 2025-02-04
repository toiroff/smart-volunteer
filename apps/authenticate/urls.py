from django.urls import path,include
from .views import RegisterView ,endpoint,VolunteersViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'volunteers', VolunteersViewSet) 

urlpatterns = [
    path('',endpoint,name="home"),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

]


 

 

 