from rest_framework import serializers


from .models import Lesson
from account.serializers import UserSerializer


class LessonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    video_length = serializers.CharField(source='get_video_length_time')

    class Meta:
        model = Lesson
        fields = [
            'uuid',
            'lesson_number'
            'user',
            'title',
            'content',
            'video_length',
            'resources',
            'file',
            'questions',
        ]


class LessonUnPaidSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    video_length = serializers.CharField(source='get_video_length_time')

    class Meta:
        model = Lesson
        fields = [
            "uuid",
            "lesson_number",
            'user',
            "title",
            "video_length",
        ]
