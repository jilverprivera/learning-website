from rest_framework import serializers


from ..models import *

from account.serializers import UserSerializer
from apps.category.api.serializer import SubCategorySerializer
from .commentSerializer import CommentSerializer
from .sectionSerializer import SectionSerializer
from .learnSerializer import LearntSerializer
from .requisiteSerializer import RequisiteSerializer


class CourseSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    subcategory = SubCategorySerializer()
    author = UserSerializer()
    sale_video = serializers.CharField(source='get_sale_video')
    stars = serializers.IntegerField(source='get_stars')
    total_stars = serializers.IntegerField(source='get_number_starts')
    total_lectures = serializers.IntegerField(source="get_total_lectures")
    total_duration = serializers.CharField(source='total_course_length')
    comments = CommentSerializer(many=True)
    sections = SectionSerializer(many=True)
    what_learnt = LearntSerializer(many=True)
    requisite = RequisiteSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "uuid",
            "title",
            "description",
            'content',
            "subcategory",
            "author",
            "thumbnail",
            "sale_video",
            "price",
            "compare_price",
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
            "what_learnt",
            "requisite",
        ]


class CourseDisplaySerializer(serializers.Serializer):
    author = UserSerializer()
    subcategory = SubCategorySerializer()
    stars = serializers.IntegerField(source='get_stars')
    sale_video = serializers.CharField(source='get_sale_video')
    thumbnail = serializers.CharField(source='get_thumbnail')

    class Meta:
        model = Course
        fields = [
            'uuid',
            'subcategory',
            'author',
            'title',
            'description',
            'course_type'
            'price'
            'stars',
            'thumbnail',
            'sale_video',
            'best_seller'
        ]
