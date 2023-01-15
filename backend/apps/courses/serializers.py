from rest_framework import serializers


from .models import Course
from account.serializers import UserSerializer
from apps.category.serializers import SubCategorySerializer
from apps.comments.serializers import CommentSerializer
from apps.sections.serializers import SectionSerializer
from apps.learnings.serializers import LearningSerializer
from apps.requisites.serializers import RequisiteSerializer


class CourseDisplayListSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    subcategory = SubCategorySerializer()
    stars = serializers.IntegerField(source='get_stars')
    thumbnail = serializers.CharField(source='get_thumbnail')
    sale_video = serializers.CharField(source='get_sale_video')

    class Meta:
        model = Course
        fields = [
            'uuid',
            'subcategory',
            'author',
            'title',
            'description',
            'course_type',
            'price',
            'discount_price',
            'discount_time',
            'stars',
            'thumbnail',
            'sale_video',
            'best_seller'
        ]


class CourseAdminListSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    subcategory = SubCategorySerializer()
    stars = serializers.IntegerField(source='get_stars')
    thumbnail = serializers.CharField(source='get_thumbnail')
    sale_video = serializers.CharField(source='get_sale_video')
    course_length = serializers.CharField(source='get_total_course_length')

    class Meta:
        model = Course
        fields = [
            'uuid',
            'subcategory',
            'author',
            'title',
            'description',
            'content',
            'thumbnail',
            'sale_video',
            'course_type',
            'price',
            'discount_price',
            'discount_time',
            'sold',
            'course_length',
            'best_seller'
            'stars',
            'total_stars',
            'status',
        ]


class CourseStudySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    subcategory = SubCategorySerializer()
    thumbnail = serializers.CharField(source='get_thumbnail')
    sale_video = serializers.CharField(source='get_sale_video')
    stars = serializers.IntegerField(source='get_stars')
    total_stars = serializers.IntegerField(source='get_number_starts')
    total_lectures = serializers.IntegerField(source="get_total_lectures")
    total_duration = serializers.CharField(source='total_course_length')

    comments = CommentSerializer(many=True)
    sections = SectionSerializer(many=True)
    learnings = LearningSerializer(many=True)
    requisite = RequisiteSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "uuid",
            "title",
            "description",
            'content',
            "author",
            "subcategory",
            "thumbnail",
            "sale_video",
            "price",
            "discount_price",
            "course_type",
            "sold",
            "course_length",
            "best_seller",
            "stars",
            "total_stars",
            "total_lectures",
            "total_duration",
            "comments",
            "sections",
            "learnings",
            "requisite",
        ]
