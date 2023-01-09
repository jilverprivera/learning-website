from rest_framework import serializers
from ..models import SubCategory, Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='get_slug')

    class Meta:
        model = Category
        fields = (
            'uuid',
            'name',
            'slug',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='get_slug')
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = (
            'uuid',
            'name',
            'slug',
            'category',
        )
