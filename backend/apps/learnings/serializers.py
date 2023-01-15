from rest_framework import serializers

from apps.learnings.models import Learning


class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning
        fields = [
            'uuid',
            'user',
            'content',
            'date_created',
        ]
