from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from apps.lessons.models import Lesson

from apps.questions.serializer import QuestionSerializer


class QuestionsListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        try:
            if Question.objects.all().count() == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)
            questions = Question.objects.all()
            serialized_questions = QuestionSerializer(questions, many=True)
            return Response(serialized_questions.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error': 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionsByUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        try:
            user = self.request.user
            questions = Question.objects.filter(user=user).all()
            serialized_questions = QuestionSerializer(questions, many=True)
            return Response(serialized_questions.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error': 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            user = self.request.user
            data = request.data
            lesson_uuid = data['lesson_uuid']
            title = data['title']
            message = data['message']
            lesson = get_object_or_404(Lesson, uuid=lesson_uuid)

            question = Question(
                user=user,
                lesson=lesson,
                title=title,
                message=message,
                accepted_answer=False
            )
            question.save()
            serialized_question = QuestionSerializer(question)
            return Response(serialized_question.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response({'Error': 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, format=None):
        try:
            user = self.request.user
            data = request.data

            question_uuid = data['question_uuid']
            title = data['title']
            message = data['message']
            question = get_object_or_404(Question, uuid=question_uuid)
            if not user == question.user:
                return Response({'Error': 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            question.title = title
            question.message = message
            question.save()
            serialized_question = QuestionSerializer(question)

            return Response(serialized_question.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error': 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, question_uuid, format=None):
        try:
            user = self.request.user
            if not Question.objects.filter(uuid=question_uuid).exists():
                return Response({'Error': 'Question with UUID: {} does not exist.'.format(question_uuid)}, status=status.HTTP_400_BAD_REQUEST)
            question = Question.objects.get(uuid=question_uuid)
            if not user == question.user:
                return Response({'Error': 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)
            question.delete()

            return Response({'Message': 'Question deleted successfully.'}, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error': 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
