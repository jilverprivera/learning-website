from rest_framework import serializers


from .models import Question
from account.serializers import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'title',
            'message',
            'accepted_answer',
            'date_created',
        ]
