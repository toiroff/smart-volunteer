from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Assigned", "Assigned"), ("Completed", "Completed")])
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks_created")
    volunteers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="tasks_assigned",
        limit_choices_to={"role": "Volunteer"}  
    )

    def __str__(self):
        return self.title