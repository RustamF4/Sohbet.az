from django.db import models # type: ignore
from django.utils import timezone  # type: ignore
from django.contrib.auth.models import User # type: ignore


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
    profile_picture = models.ImageField(upload_to='media/uploads/profile_pictures', default='media/uploads/profile_pictures/default.png', blank=True)
    wall_picture = models.ImageField(upload_to= 'media/uploads/wall_pictures', default= 'media/uploads/wall_pictures/default.webp')