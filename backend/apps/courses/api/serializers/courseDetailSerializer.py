# from rest_framework import serializers

# from apps.courses.models import Course

# from account.serializers import UserSerializer
# from apps.category.api.serializer import SubCategorySerializer


# class CourseDetailSerializer(serializers.ModelSerializer):
#     author = UserSerializer()
#     subcategory = SubCategorySerializer()
#     thumbnail = serializers.CharField(source='get_thumbnail')
#     stars = serializers.IntegerField(source='get_stars')
#     total_stars = serializers.IntegerField(source='get_number_starts')
#     total_lectures = serializers.IntegerField(source="get_total_lectures")
#     total_duration = serializers.CharField(source='total_course_length')

#     class Meta:
#         model = Course
#         fields = [
#             'uuid',
#             'subcategory',
#             'author',
#             'title',
#             'description',
#             'stars',
#             'thumbnail',
#             'total_stars',
#             'total_lectures',
#             'total_duration',
#         ]
