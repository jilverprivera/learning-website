from django.urls import path

from apps.questions.views import QuestionsListView

urlpatterns = [
    path('questions/', QuestionsListView.as_view())
]
