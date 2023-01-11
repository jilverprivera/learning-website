from rest_framework import serializers

from apps.courses.models import Question


class QuestionAnswerSerializer(serializers.ModelSerializer):
    answer_count = serializers.CharField(source='get_answers_count')

    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'title',
            'message',
            'answer_count',
            'accepted_answer',
            'date_created',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionAnswerSerializer()
    positive_votes = serializers.CharField(source='calculate_positive_votes')
    negative_votes = serializers.CharField(source='calculate_negative_votes')
    votes = serializers.CharField(source='calculate_votes')

    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'question',
            'message',
            'is_accepted_answer',
            'votes',
            'positive_votes',
            'negative_votes',
            'date_created',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    get_answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'uuid',
            'user',
            'title',
            'message',
            'accepted_answer',
            'get_answers_count',
            'get_answers'
            'date_created',
        ]
