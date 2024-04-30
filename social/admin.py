from django.contrib import admin # type: ignore
from .models import Post, Profile

admin.site.register(Post)
admin.site.register(Profile)
