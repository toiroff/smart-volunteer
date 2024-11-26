from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer

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
