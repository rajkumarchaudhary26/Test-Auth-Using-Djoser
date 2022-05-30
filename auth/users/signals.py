from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from . import models as app_models
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from .models import Profile, User

@receiver(post_save, sender = User, dispatch_uid = 'create_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User, dispatch_uid = 'save user profile')
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Profile, dispatch_uid = 'warm profile picture')
def warm_Profile_pic(sender, instance, **kwargs):
    if instance.profile_pic:
        profile_img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=instance,
            rendition_key_set='profile_picture',
            image_attr='profile_pic'
        )
        num_created, failed_to_create = profile_img_warmer.warm()

