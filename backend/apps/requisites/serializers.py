from rest_framework import serializers

from .models import Requisite
from account.serializers import UserSerializer


class RequisiteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Requisite
        fields = [
            'uuid',
            'user',
            'title',
            'description',
            'date_created',
        ]
