from django.urls import path

from apps.answers.views import AnswerListView

urlpatterns = [
    path('answers/', AnswerListView.as_view())
]
