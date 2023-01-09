from rest_framework import serializers

from apps.courses.models import Section
from .lessonSerializer import LessonSerializer


class SectionSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    total_duration = serializers.CharField(source='total_length')

    class Meta:
        model = Section
        fields = [
            "uuid"
            "user",
            'title',
            "section_number",
            "lessons",
            "total_duration",
        ]
