from rest_framework import serializers
from apps.courses.models import WhatLearnt


class LearntSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatLearnt
        fields = [
            "id",
            'uuid',
            'user',
            "title",
            'description',
            'date_created',
        ]
