from django.urls import path

from .api.views.courses import *

urlpatterns = [
    path("courses", CoursesDisplayListView.as_view()),
    path("course/detail/<uuid:course_uuid>/", CourseDetailView.as_view()),
]
