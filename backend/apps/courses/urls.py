from django.urls import path

from .views import *


urlpatterns = [
    path("courses", CoursesDisplayListView.as_view()),
    path('course/create/', CreateCourseView.as_view()),
    path('course/publish/<uuid:course_uuid>', PublishCourseView.as_view()),
]
