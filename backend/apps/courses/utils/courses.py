from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status

from apps.courses.models import Course
from apps.category.models import SubCategory
from account.models import User


def get_courses_list(request):
    sort_by = request.query_params.get('sort_by')
    order = request.query_params.get('order')
    limit = request.query_params.get('limit')

    if not (sort_by == 'date_created' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'title' or sort_by == 'course_type'):
        sort_by = 'date_created'

    if limit:
        try:
            limit = int(limit)
        except:
            return Response({'Error': 'Limit must be an integer.'}, status=status.HTTP_404_NOT_FOUND)

    if order == 'desc':
        sort_by = '-' + sort_by
        courses = Course.objects.order_by(
            sort_by).all().filter(status="published")[:int(limit)]
    elif order == 'asc':
        courses = Course.objects.order_by(
            sort_by).all().filter(status="published")[:int(limit)]
    else:
        courses = Course.objects.all().filter(status="published")

    return courses


def create_course(self, request):

    data = self.request.data
    account = data['account']
    subcategory = data['subcategory_uuid']
    title = data['title']
    description = data['description']
    content = data['content']
    thumbnail = data['thumbnail']
    sale_video = data['sale_video']
    course_type = data['course_type']
    price = data['price']
    compare_price = data['compare_price']

    if price.find(".") == -1:
        price = price + ".0"

    author = get_object_or_404(User, account=account)
    subcategory = get_object_or_404(SubCategory, id=subcategory)

    course = Course(
        title=title,
        description=description,
        content=content,
        thumbnail=thumbnail,
        sale_video=sale_video,
        subcategory=subcategory,
        author=author,
        course_type=course_type,
        price=price,
        compare_price=compare_price
    )
    course.save()

    return Response({'success': 'Message sent successfully'})
