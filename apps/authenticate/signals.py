from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=UserProfile,weak=False)
def user_profile(sender, instance, created, **kwargs):
    if created:   
        if instance.role == "Volunteer":
            group, _ = Group.objects.get_or_create(name='Volunteers')   
            instance.groups.add(group)  

        elif instance.role == "Requester":
            group, _ = Group.objects.get_or_create(name='Requesters')   
            instance.groups.add(group)  
        print("Group Added")

 