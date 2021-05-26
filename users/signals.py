from django.db.models.signals import post_save  # this is a signal which gets fired when the object is saved
from django.contrib.auth.models import User  # User model is going to be a sender here
from django.dispatch import receiver  # receiver functions receives a signal and make some action after that
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
