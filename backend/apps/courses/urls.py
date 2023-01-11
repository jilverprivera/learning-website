from django.urls import path

from .api.views.course_views import *

urlpatterns = [
    path("courses", CoursesDisplayListView.as_view()),
    path("course/detail/<uuid:course_uuid>/", CourseDetailView.as_view()),
]
