from rest_framework import serializers

from .models import Question

from account.serializers import UserSerializer
from apps.lessons.serializers import LessonSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'lesson',
            'title',
            'message',
            'accepted_answer',
            'date_created',
        ]
