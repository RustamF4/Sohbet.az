from django.db import models # type: ignore
from django.utils import timezone  # type: ignore
from django.contrib.auth.models import User # type: ignore


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

