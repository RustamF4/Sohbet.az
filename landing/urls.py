from django.urls import path # type: ignore
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]
