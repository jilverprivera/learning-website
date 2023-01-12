# from django.shortcuts import get_object_or_404
# from django.core.exceptions import ValidationError

# from rest_framework.views import APIView
# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser

# from apps.courses.api.serializers.courseDisplayListSerializer import *
# from apps.courses.api.serializers.courseDetailSerializer import *
# from apps.courses.api.serializers.courseStudySerializer import *

# from apps.courses.models import Course
# from apps.category.models import SubCategory
# from account.models import User


# class CoursesDisplayListView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, format=None):
#         sort_by = request.query_params.get('sort_by')
#         order = request.query_params.get('order')
#         limit = request.query_params.get('limit')

#         if not (sort_by == 'date_created' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'title' or sort_by == 'course_type'):
#             sort_by = 'date_created'

#         if limit:
#             try:
#                 limit = int(limit)
#             except:
#                 return Response({'Error': 'Limite debe ser un número entero.'}, status=status.HTTP_404_NOT_FOUND)

#         if order == 'desc':
#             sort_by = '-' + sort_by
#             courses = Course.objects.order_by(
#                 sort_by).all().filter(status="published")[:int(limit)]
#         elif order == 'asc':
#             courses = Course.objects.order_by(
#                 sort_by).all().filter(status="published")[:int(limit)]
#         else:
#             courses = Course.objects.all().filter(status="published")

#         serialized_courses = CourseDisplayListSerializer(courses, many=True)
#         if serialized_courses:
#             return Response(serialized_courses.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'Error': 'No se han creado cursos aún.'}, status=status.HTTP_404_NOT_FOUND)


# class CourseDetailView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, course_uuid, format=None):
#         if not Course.objects.all().filter(status='published', uuid=course_uuid).exists():
#             return Response({'Error', 'No se ha encontrado el curso con dicha uuid.'}, status=status.HTTP_404_NOT_FOUND)
#         course = Course.objects.get(uuid=course_uuid)
#         serialized_course = CourseDetailSerializer(course)
#         return Response(serialized_course.data, status=status.HTTP_200_OK)


# class CourseStudyView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, uuid, format=None):
#         if not Course.objects.all().filter(status='published', uuid=uuid).exists():
#             return Response({'Error': 'Course with uuid does not exists.'}, status=status.HTTP_404_NOT_FOUND)
#         print(request.user)
#         if not request.user.is_authenticated():
#             return Response({'Error': 'User must be authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

#         user_subscription = request.user.subscriptions.pricing
#         user_subscription_status = request.user.subscriptions.status
#         course = Course.objects.get(uuid=uuid)
#         course_pricing = course.pricing_tiers.all()

#         for pricing in course_pricing:
#             if not user_subscription in pricing:
#                 return Response({'Error': 'User does not have subscription to the course'}, status=status.HTTP_400_BAD_REQUEST)

#         serialized_course = CourseStudySerializer(course)
#         return Response(serialized_course.data, status=status.HTTP_200_OK)


# class CreateCourseView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):

#         if not self.request.user.is_authenticated:
#             return Response({'Error': 'User must be authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

#         data = self.request.data
#         if not data:
#             return Response({'Error': 'Data is required.'}, status=status.HTTP_400_BAD_REQUEST)

#         user = self.request.user
#         subcategory_uuid = data['subcategory']
#         author = get_object_or_404(User, uuid=user.uuid)
#         subcategory = get_object_or_404(SubCategory, uuid=subcategory_uuid)
#         title = data['title']
#         description = data['description']
#         content = data['content']
#         thumbnail = data['thumbnail']
#         sale_video = data['sale_video']
#         course_type = data['course_type']
#         price = data['price']
#         discount_price = data['discount_price']
#         best_seller = data['best_seller']

#         if price.find(".") == -1:
#             price = price + ".0"

#         course = Course(
#             author=author,
#             subcategory=subcategory,
#             title=title,
#             description=description,
#             content=content,
#             thumbnail=thumbnail,
#             sale_video=sale_video,
#             course_type=course_type,
#             price=price,
#             discount_price=discount_price,
#             best_seller=best_seller
#         )
#         course.save()

#         return Response({'Ok', 'Course has been created succesfully.'}, status=status.HTTP_201_CREATED)


# class CreateCourseView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def put(self, request, course_uuid, format=None):
#         try:
#             return Response({'Ok', 'Course has been created succesfully.'}, status=status.HTTP_201_CREATED)

#         except ValidationError:
#             return Response({'Error', 'Something went wrong  has been created succesfully.'}, status=status.HTTP_201_CREATED)
