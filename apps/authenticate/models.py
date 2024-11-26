from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ("Requester", "Requester"),
        ("Volunteer", "Volunteer")
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Requester")

    def __str__(self):
        return self.username
