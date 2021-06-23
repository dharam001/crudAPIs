from django.urls import path
from .views import (UserCreateView, UserDeleteView, UserDetailView,
                    UserListView, UserUpdateView)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create_user', UserCreateView.as_view(), name='create-user'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
]