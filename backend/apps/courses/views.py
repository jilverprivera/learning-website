from django.shortcuts import get_object_or_404

from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from account.models import User
from apps.category.models import SubCategory
from .models import Course


from .utils.courses import *


# class CoursesListView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, format=None):
#         courses = get_courses_list(request)
#         serialized_courses = CourseListSerializer(courses, many=True)
#         if serialized_courses:
#             return Response(serialized_courses.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'Error': 'Courses not created yet.'}, status=status.HTTP_404_NOT_FOUND)


# class CreateCourseView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         create_course(self, request)
#         return Response({'success': 'Message sent successfully'})


# class CourseView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, uuid, format=None):
#         if not Course.objects.all().filter(status='published', uuid=uuid).exists():
#             return Response({'Error': 'Course with uuid does not exists.'}, status=status.HTTP_404_NOT_FOUND)
#         print(request.user)
#         # if not request.user.is_authenticated():
#         #     return Response({'Error': 'User must be authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

#         # user_subscription = request.user.subscriptions.pricing
#         # user_subscription_status = request.user.subscriptions.status
#         course = Course.objects.get(uuid=uuid)
#         # course_pricing = course.pricing_tiers.all()

#         # for pricing in course_pricing:
#         #     if not user_subscription in pricing:
#         #         return Response({'Error': 'User does not have subscription to the course'}, status=status.HTTP_400_BAD_REQUEST)

#         serialized_course = CourseSerializer(course)
#         return Response(serialized_course.data, status=status.HTTP_200_OK)
