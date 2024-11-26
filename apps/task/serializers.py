from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,StringRelatedField
from .models import Task
from django.contrib.auth import get_user_model
from apps.authenticate.serializers import UserProfileSerializer
from apps.authenticate.models import UserProfile

 

class TaskSerializer(ModelSerializer):
      
 
    volunteers=  PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        many=True,
     
    )
  
    class Meta:
        model = Task
        fields = '__all__'

    