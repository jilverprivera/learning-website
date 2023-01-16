from django.urls import path

from apps.answers.views import *

urlpatterns = [
    path('answers/', AnswerListView.as_view(), 'GET_ALL_ANSWERS'),

    path('answer/<uuid:question_uuid>/create/', CreateAnswerView.as_view(), name='CREATE_QUESTION_ANSWER'),
    path('answer/<uuid:answer_uuid>/update/', UpdateAnswerMessageView.as_view(), name='UPDATE_ANSWER_MESSAGE'),
    path('answer/<uuid:answer_uuid>/accept/', AcceptAnswerView.as_view(), name='ACCEPT_QUESTION_ANSWER'),
    path('answer/<uuid:answer_uuid>/delete/', DeleteAnswerView.as_view(), name='DELETE_ANSWER'),
]
