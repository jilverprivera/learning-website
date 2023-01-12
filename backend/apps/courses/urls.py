from django.urls import path

from .api.views.course_views import *
from .api.views.comment_views import *
from .api.views.question_views import *


urlpatterns = [
    # path("courses", CoursesDisplayListView.as_view()),
    # path("course/detail/<uuid:course_uuid>/", CourseDetailView.as_view()),

    # # path("comment/create/<uuid:course_uuid>/", AddCommentView.as_view()),
    # # path("comment/update/<uuid:course_uuid>/", UpdateCommentView.as_view()),
    # # path("comment/delete/<uuid:course_uuid>/", DeleteCommentView.as_view()),
    
    # path("question/create/<uuid:lesson_uuid>/", CreateQuestionView.as_view()),
]
