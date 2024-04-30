from django.urls import path  # type: ignore
from .views import PostView, PostDetailView, ProfileView

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]
