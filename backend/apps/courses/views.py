from django.shortcuts import get_object_or_404

from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from account.models import User
from apps.category.models import SubCategory
from .models import Course

from .serializers.courseSerializer import CourseSerializer

from .utils.courses import *


class CoursesListView(APIView):
    def get(self, request, format=None):
        courses = get_courses_list(request)
        serialized_courses = CourseSerializer(courses, many=True)
        if serialized_courses:
            return Response(serialized_courses.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Courses not created yet.'}, status=status.HTTP_404_NOT_FOUND)


class CreateCourseView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        create_course(self, request)
        return Response({'success': 'Message sent successfully'})
