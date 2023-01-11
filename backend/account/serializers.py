from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(ModelSerializer):
    image = serializers.CharField(source='get_image')

    class Meta:
        model = User
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'stripe_customer_id',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'image',
        )
