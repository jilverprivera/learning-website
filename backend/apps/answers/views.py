from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.answers.serializers import AnswerSerializer

from .models import Answer


class AnswerListView(APIView):
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

    def post(self, request, format=None):
        try:
            user = self.request.user
            data = request.data

            if not user.is_authenticated():
                return Response({'Error', 'User need to be authenticated.'}, status=status.HTTP_400_BAD_REQUEST)
            if not data():
                return Response({'Error', 'Data is required.'}, status=status.HTTP_400_BAD_REQUEST)

            question = data['question_uuid']
            message = data['message']
            accepted_answer = data['accepted_answer']

            answer = Answer(
                user=user,
                question=question,
                message=message,
                accepted_answer=accepted_answer
            )
            answer.save()

            return Response(answer, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except ValidationError:
            return Response({'Error', 'Something went wrong getting questions.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, answer_uuid, format=None):
        try:
            user = self.request.user
            answer = get_object_or_404(Answer, uuid=answer_uuid)

            if not user():
                return Response({'Error', 'User credentials not found.'}, status=status.HTTP_400_BAD_REQUEST)
            if not user.uuid ==answer.user.uuid:
                return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            data = request.data
            answer.message = data['message']
            answer.accepted_answer = data['accepted_answer']
            answer.save()
            return Response(answer, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except ValidationError:
            return Response({'Error', 'Something went wrong updating the answer.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request,answer_uuid, format=None):
        try:
            user = self.request.user
            data = request.data
            answer = get_object_or_404(Answer, uuid=answer_uuid)

            if not user.uuid ==answer.user.uuid:
                return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

            confirm_delete=data['confirm_delete']
            if confirm_delete :
                answer.delete()

            return Response({'success': 'Message sent successfully'})
        except:
            return Response({'error': 'Message failed to be sent'})