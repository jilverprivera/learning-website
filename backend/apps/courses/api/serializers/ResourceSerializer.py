from rest_framework import serializers
from apps.courses.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Resource
        fields = [
            'uuid',
            'user',
            "title",
            'file',
            'url',
        ]