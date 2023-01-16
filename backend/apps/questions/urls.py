from django.urls import path

from apps.questions.views import *

urlpatterns = [
    path('questions/', QuestionsListView.as_view()),
    path('questions/self/', QuestionsByUserView.as_view()),

    path('question/create/', AddQuestionView.as_view()),
    path('question/update/', UpdateQuestionView.as_view()),
    path('question/<uuid:question_uuid>/delete/', DeleteQuestionView.as_view()),

]
