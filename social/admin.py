from django.contrib import admin # type: ignore
from .models import Post

admin.site.register(Post)
