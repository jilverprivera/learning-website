from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Question
from apps.questions.serializer import QuestionSerializer


class QuestionsListView(APIView):
    def get(self, request, format=None):
        try:
            if Question.objects.all().count() == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)
            questions = Question.objects.all()
            serialized_questions = QuestionSerializer(questions, many=True)
            return Response(serialized_questions.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong. Please contact an administrator.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            user = self.request.user
            data = request.data

            lesson = data['lesson']
            message = data['message']
            title = data['title']
            accepted_answer = data['accepted_answer']

            question = Question(
                user=user,
                lesson=lesson,
                title=title,
                message=message,
                accepted_answer=accepted_answer
            )
            question.save()
            return Response(question, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response({'Error', 'Something went wrong getting questions.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, question_uuid, format=None):
        try:
            user = self.request.user
            data = request.data

            if not Question.objects.filter(uuid=question_uuid).exists():
                return Response({'Error', 'Question with uuid: {} not found.'.format(question_uuid)}, status=status.HTTP_404_NOT_FOUND0)
            question = Question.objects.get(uuid=question_uuid)

            if not user.uuid == question.user.uuid:
                return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            title = data['title']
            message = data['message']
            accepted_answer = data['accepted_answer']

            question.title = title
            question.message = message
            question.accepted_answer = accepted_answer
            question.save()
            return Response(question, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response({'Error', 'Something went wrong getting questions.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, question_uuid, format=None):
        try:
            user = self.request.user
            data = request.data
            question = get_object_or_404(Question, uuid=question_uuid)

            if not user.uuid == question.user.uuid:
                return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            confirm_delete = data['confirm_delete']
            if confirm_delete:
                question.delete()

            return Response({'Success': 'Question deleted successfully.'}, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'Error', 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
