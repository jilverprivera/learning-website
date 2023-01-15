from rest_framework import serializers

from .models import Answer

from account.serializers import UserSerializer
from apps.questions.serializer import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = [
            'uuid',
            'user',
            'question',
            'message',
            'accepted_answer',
            'date_created',
        ]
