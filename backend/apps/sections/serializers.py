from rest_framework import serializers


from .models import Section
from account.serializers import UserSerializer


class SectionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    total_length = serializers.CharField(source='total_length')

    class Meta:
        model = Section
        fields = [
            'id',
            'uuid',
            'user',
            'title',
            'section_number',
            'total_length',
            'lessons',
            'date_created',
        ]
