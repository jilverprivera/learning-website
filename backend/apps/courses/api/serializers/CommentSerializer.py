# from rest_framework.serializers import SerializerMethodField
# from rest_framework import serializers

# # from apps.courses.models import Comment


# # class CommentSerializer(serializers.ModelSerializer):
# #     first_name = SerializerMethodField()
# #     full_name = SerializerMethodField()
# #     email = SerializerMethodField()
# #     user_image = SerializerMethodField()

# #     class Meta:
# #         model = Comment
# #         fields = (
# #             'uuid',
# #             'email',
# #             'first_name',
# #             'full_name',
# #             'user_image',
# #             'star_number',
# #             'message',
# #             'date_created',
# #         )

# #     def get_email(self, obj):
# #         return obj.user.email

# #     def get_first_name(self, obj):
# #         return obj.user.first_name

# #     def get_full_name(self, obj):
# #         return obj.user.first_name + ' ' + obj.user.last_name

# #     def get_user_image(self, obj):
# #         return obj.user.image.url
