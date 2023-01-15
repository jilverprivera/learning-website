from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'uuid',
            'full_name',
            'user_image',
            'star_number',
            'message',
            'date_created'
        ]

    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_user_image(self, obj):
        return obj.user.image.url
