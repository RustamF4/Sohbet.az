from django.db import models # type: ignore
from django.utils import timezone  # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.db.models.signals import post_save, pre_save # type: ignore
from django.dispatch import receiver # type: ignore

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='media/uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
    wall_picture = models.ImageField(upload_to= 'media/uploads/wall_pictures', default= 'uploads/wall_pictures/default.jpg')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()