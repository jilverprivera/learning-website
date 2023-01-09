from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Category, SubCategory
from .api.serializer import CategorySerializer, SubCategorySerializer


class CategoryListView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        sort_by = request.query_params.get('sort_by')
        if not (sort_by == 'created_at' or sort_by == 'name'):
            sort_by = '-created_at'
        categories = Category.objects.order_by(sort_by).all()
        serialized_categories = CategorySerializer(categories, many=True)
        if serialized_categories:
            return Response(serialized_categories.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No categories found.'}, status=status.HTTP_404_NOT_FOUND)


class LatestCategoriesView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        categories = Category.objects.order_by('-created_at').all()[0:4]
        serialized_categories = CategorySerializer(categories, many=True)
        if serialized_categories:
            return Response(serialized_categories.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No categories found.'}, status=status.HTTP_404_NOT_FOUND)


class CategoryView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except:
            return Response({'Error': 'ID must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
        if Category.objects.filter(id=pk).exists():
            categories = Category.objects.filter(id=pk)
            serialized_categories = CategorySerializer(categories, many=True)
            if serialized_categories:
                return Response(serialized_categories.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'No categories found.'}, status=status.HTTP_404_NOT_FOUND)


# -------------------------------- SUB CATEGORIES -------------------------------- #

class SubCategoriesListView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        sort_by = request.query_params.get('sort_by')
        if not (sort_by == 'created_at' or sort_by == 'name'):
            sort_by = 'created_at'
        sub_categories = SubCategory.objects.order_by(sort_by).all()
        serialized_sub_categories = SubCategorySerializer(
            sub_categories, many=True)
        if serialized_sub_categories:
            return Response(serialized_sub_categories.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No sub categories found.'}, status=status.HTTP_404_NOT_FOUND)


class SubCategoryView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except:
            return Response({'Error': 'ID must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
        if SubCategory.objects.filter(id=pk).exists():
            sub_category = SubCategory.objects.filter(id=pk)
            serialized_sub_category = SubCategorySerializer(
                sub_category, many=True)
            if serialized_sub_category:
                return Response(serialized_sub_category.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'No categories found.'}, status=status.HTTP_404_NOT_FOUND)


class SubCategoryByPrincipalView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, principal, format=None):
        print(principal)
        try:
            principal = int(principal)
        except:
            return Response({'Error': 'ID must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
        if SubCategory.objects.filter(principal=principal).exists():
            sub_categories = SubCategory.objects.filter(principal=principal)
            serialized_sub_categories = SubCategorySerializer(
                sub_categories, many=True)
            if serialized_sub_categories:
                return Response(serialized_sub_categories.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'No sub categories found.'}, status=status.HTTP_404_NOT_FOUND)
