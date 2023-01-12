# from rest_framework import serializers

# from apps.courses.models import *

# from account.serializers import UserSerializer
# from apps.category.api.serializer import SubCategorySerializer


# class CourseDisplayListSerializer(serializers.ModelSerializer):
#     author = UserSerializer()
#     subcategory = SubCategorySerializer()
#     stars = serializers.IntegerField(source='get_stars')
#     thumbnail = serializers.CharField(source='get_thumbnail')
#     sale_video = serializers.CharField(source='get_sale_video')

#     class Meta:
#         model = Course
#         fields = [
#             'uuid',
#             'subcategory',
#             'author',
#             'title',
#             'description',
#             'course_type',
#             'price',
#             'discount_price',
#             'stars',
#             'thumbnail',
#             'sale_video',
#             'best_seller'
#         ]





# # class CourseUnPaidSerializer(serializers.ModelSerializer):
# #     thumbnail = serializers.CharField(source='get_thumbnail')
# #     subcategory = SubCategorySerializer()
# #     author = UserSerializer()
# #     sale_video = serializers.CharField(source='get_sale_video')
# #     stars = serializers.IntegerField(source='get_stars')
# #     total_stars = serializers.IntegerField(source='get_number_starts')
# #     total_lectures = serializers.IntegerField(source="get_total_lectures")
# #     total_duration = serializers.CharField(source='total_course_length')

# #     class Meta:
# #         model = Course
# #         fields = [
# #             "uuid",
# #             "title",
# #             "description",
# #             'content',
# #             "subcategory",
# #             "author",
# #             "thumbnail",
# #             "sale_video",
# #             "price",
# #             "compare_price",
# #             "course_type",
# #             "sold",
# #             "course_length",
# #             "best_seller",
# #             "stars",
# #             "total_stars",
# #             "total_lectures",
# #             "total_duration",
# #         ]
