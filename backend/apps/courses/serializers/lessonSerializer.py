from rest_framework import serializers

from apps.courses.models import Lesson


class LessonSerializer(serializers.Serializer):
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
