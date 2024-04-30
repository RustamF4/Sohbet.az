from django.urls import path  # type: ignore
from .views import PostView, PostDetailView, ProfileView, ProfileEditView

urlpatterns = [
    path('', PostView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile_edit')
]
