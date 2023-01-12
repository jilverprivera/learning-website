# from django.shortcuts import get_object_or_404

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from backend.apps.courses.models import Answer


# class VoteAnswerView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def put(self, request, answer_uuid, format=None):
#         data = self.request.data
#         user = self.request.user

#         answer = get_object_or_404(Answer, uuid=answer_uuid)
#         if not answer:
#             return Response({'Error', 'Answer with uuid: {} not found'.format(answer_uuid)}, status=status.HTTP_404_NOT_FOUND)
#         answer.user = user
#         answer.votes = data['vote']