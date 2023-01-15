from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Lesson
from apps.sections.models import Section

from .serializers import LessonSerializer, LessonUnPaidSerializer


class CreateLessonView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, section_uuid, format=None):
        section = get_object_or_404(Section, uuid=section_uuid)
        if not section:
            return Response({'Error', 'Section with uuid: {} not found.'.format(section_uuid)}, status=status.HTTP_404_NOT_FOUND)

        data = self.request.data
        user_id = data['user_id']
        section_id = section
        title = data['title']
        file = data['file']
        content = data['content']
        lesson_number = data['lesson_number']

        lesson = Lesson(
            user=user_id,
            section=section_id,
            title=title,
            file=file,
            content=content,
            lesson_number=lesson_number
        )

        lesson.save()
