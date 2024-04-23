from django.urls import path  # type: ignore
from .views import PostView
from.views import PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
