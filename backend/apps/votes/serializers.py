from rest_framework import serializers


from .models import Vote
from account.serializers import UserSerializer


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vote
        fields = [
            'uuid',
            'user',
            'vote',
            'date_created'
        ]

    def get_email(self, obj):
        return obj.user.email
