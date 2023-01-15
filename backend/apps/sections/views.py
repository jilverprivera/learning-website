from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Section
from account.models import User
from apps.courses.models import Course

from apps.sections.serializers import SectionSerializer


class SectionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        sections = Section.objects.order_by('user', 'section_number').all()
        serialized_sections = SectionSerializer(sections, many=True)
        return Response(serialized_sections.data, status=status.HTTP_200_OK)


class CreateSectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_uuid, format=None):
        try:
            course = get_object_or_404(Course, uuid=course_uuid)
            user = self.request.user
            user = get_object_or_404(User, uuid=user.uuid)

            data = self.request.data
            title = data['title']
            section_number = data['section_number']
            section = Section(
                user=user,
                title=title,
                section_number=section_number,
            )
            section.save()
            course.sections = section
            course.save()
            serialized_section = SectionSerializer(section)
            return Response(serialized_section.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateSectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, section_uuid, format=None):
        try:
            section = get_object_or_404(Section, uuid=section_uuid)
            user = self.request.user
            if not section.user.uuid == user.uuid:
                return Response({'Error', 'User credentials do not match with section.'}, status=status.HTTP_400_BAD_REQUEST)

            data = self.request.data
            title = data['title']
            section_number = data['section_number']
            section.title = title
            section.section_number = section_number
            section.save()
            serialized_section = SectionSerializer(section)
            return Response(serialized_section.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateSectionNumberView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, section_uuid, format=None):
        try:
            section = get_object_or_404(Section, uuid=section_uuid)
            user = self.request.user

            if not section.user.uuid == user.uuid:
                return Response({'Error', 'User credentials do not match with section.'}, status=status.HTTP_400_BAD_REQUEST)

            data = self.request.data
            section_number = data['section_number']
            section.section_number = section_number
            section.save()
            serialized_section = SectionSerializer(section)
            return Response(serialized_section.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteSectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, section_uuid, format=None):
        try:
            section = get_object_or_404(Section, uuid=section_uuid)
            user = self.request.user

            if not section.user.uuid == user.uuid:
                return Response({'Error', 'User credentials do not match with section.'}, status=status.HTTP_400_BAD_REQUEST)
            section.delete()
            return Response({'Success', 'Section has been deleted successfully.'}, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
