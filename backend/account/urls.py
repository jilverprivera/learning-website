from django.urls import path

from .views import getUserByID, getUserByEmail, users

urlpatterns = [
    path("users/", users, name="get_users"),
    path("user/<str:pk>/", getUserByID, name="get_user_id"),
]
