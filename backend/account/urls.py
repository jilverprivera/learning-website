from django.urls import path

from .views import *

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("user/<str:pk>/", SingleUserView.as_view()),
]
