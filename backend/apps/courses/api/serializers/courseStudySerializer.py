# from rest_framework import serializers

# from apps.courses.models import Course

# from account.serializers import UserSerializer
# from apps.category.api.serializer import SubCategorySerializer
# # from apps.courses.api.serializers.CommentSerializer import CommentSerializer
# # from apps.courses.api.serializers.LearnSerializer import LearnSerializer
# # from apps.courses.api.serializers.RequisiteSerializer import RequisiteSerializer
# # from apps.courses.api.serializers.SectionSerializer import SectionSerializer


# class CourseStudySerializer(serializers.ModelSerializer):
#     thumbnail = serializers.CharField(source='get_thumbnail')
#     subcategory = SubCategorySerializer()
#     author = UserSerializer()
#     sale_video = serializers.CharField(source='get_sale_video')
#     stars = serializers.IntegerField(source='get_stars')
#     total_stars = serializers.IntegerField(source='get_number_starts')
#     total_lectures = serializers.IntegerField(source="get_total_lectures")
#     total_duration = serializers.CharField(source='total_course_length')

#     # comments = CommentSerializer(many=True)
#     # sections = SectionSerializer(many=True)
#     # what_learnt = LearnSerializer(many=True)
#     # requisite = RequisiteSerializer(many=True)

#     class Meta:
#         model = Course
#         fields = [
#             "uuid",
#             "title",
#             "description",
#             'content',
#             "subcategory",
#             "author",
#             "thumbnail",
#             "sale_video",
#             "price",
#             "discount_price",
#             "course_type",
#             "sold",
#             "course_length",
#             "best_seller",
#             "stars",
#             "total_stars",
#             "total_lectures",
#             "total_duration",
#             "comments",
#             "sections",
#             "what_learnt",
#             "requisite",
#         ]
