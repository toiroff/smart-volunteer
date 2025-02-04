from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .models import UserProfile
from .serializers import RegisterSerializer,UserProfileSerializer
 


@api_view(['GET'])
@cache_page(60*15)
def endpoint(request):
 
  data = ['/register','/login','/tasks','/volunteers','/volunteers/id']


  return Response(data)


class VolunteersViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = UserProfile.objects.filter(role="Volunteer")
    serializer_class = RegisterSerializer



class RegisterView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer


    def perform_create(self, serializer):
        user = serializer.save()
        return Response({
            'username': user.username,
            'role': user.role,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
