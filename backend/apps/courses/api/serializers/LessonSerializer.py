from rest_framework import serializers

from apps.courses.models import Lesson


class LessonSerializer(serializers.Serializer):
    length = serializers.CharField(source='get_video_length_time')

    class Meta:
        model = Lesson
        fields = [
            'uuid',
            'lesson_number'
            'user',
            'title',
            'content',
            'length',
            'resources',
            'file',
            'questions',
        ]


class LessonUnPaidSerializer(serializers.ModelSerializer):
    length = serializers.CharField(source='get_video_length_time')

    class Meta:
        model = Lesson
        fields = [
            "uuid",
            "lesson_number",
            'user',
            "title",
            "length",
        ]
