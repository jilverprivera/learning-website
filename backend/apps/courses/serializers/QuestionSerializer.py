from rest_framework import serializers

from apps.courses.models import Question


class QuestionAnswerSerializer(serializers.ModelSerializer):
    answer_count = serializers.CharField(source="get_answers_count")
    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'title',
            'message',
            'answer_count',
            'accepted_answer',
            'created_at',
        ]
