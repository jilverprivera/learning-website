from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Answer
from apps.questions.models import Question

from apps.answers.serializers import AnswerSerializer


class AnswerListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        try:
            if Answer.objects.all().count() == 0:
                return Response({}, status=status.HTTP_204_NO_CONTENT)

            answers = Answer.objects.all()
            serialized_answers = AnswerSerializer(answers, many=True)
            return Response(serialized_answers.data, status=status.HTTP_200_OK)

        except ValidationError:
            return Response({'Error', 'Something went wrong getting questions.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, question_uuid, format=None):
        try:
            user = self.request.user
            data = request.data
            question = get_object_or_404(Question, uuid=question_uuid)
            message = data['message']

            answer = Answer(
                user=user,
                question=question,
                message=message,
                accepted=False
            )
            answer.save()

            return Response(answer, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except ValidationError:
            return Response({'Error', 'Something went wrong getting questions.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateAnswerMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, answer_uuid, format=None):
        try:
            user = self.request.user
            answer = get_object_or_404(Answer, uuid=answer_uuid)

            if not answer.user.uuid == user.uuid:
                return Response({'Error', 'User credentials do not match the answer.'}, status=status.HTTP_400_BAD_REQUEST)

            data = request.data
            answer.message = data['message']
            answer.save()
            return Response(answer, status=status.HTTP_200_OK)

        except ValidationError:
            return Response({'Error', 'Something went wrong updating the answer.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AcceptAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, answer_uuid, format=None):
        user = self.request.user
        if not user.is_staff or user.is_superuser:
            return Response({'Error', 'User does not have permissions.'}, status=status.HTTP_400_BAD_REQUEST)

        answer = get_object_or_404(Answer, uuid=answer_uuid)
        question = get_object_or_404(Question, uuid=answer.question.uuid)

        answer.accepted = True
        answer.save()
        question.accepted_answer = True
        question.save()
        return Response(answer, status=status.HTTP_200_OK)


class DeleteAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, answer_uuid, format=None):
        try:
            user = self.request.user
            data = request.data
            answer = get_object_or_404(Answer, uuid=answer_uuid)

            if not user.uuid == answer.user.uuid:
                return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            confirm_delete = data['confirm_delete']
            if confirm_delete:
                answer.delete()

            return Response({'success': 'Message sent successfully'})
        except:
            return Response({'error': 'Message failed to be sent'})
