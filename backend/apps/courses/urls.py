from django.urls import path

from .views import *

urlpatterns = [
    path("courses", CoursesListView.as_view()),
]
