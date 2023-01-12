# from django.shortcuts import get_object_or_404

# from rest_framework import permissions, status
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from apps.courses.models import Course
# # from apps.courses.models import Comment
# # from apps.courses.api.serializers.CommentSerializer import CommentSerializer

# import json


# # class AddCommentView(APIView):
# #     permission_classes = [permissions.IsAuthenticated]

# #     def post(self, request, course_uuid, *args, **kwargs):
# #         try:
# #             course = Course.objects.all().filter(status='published').get(uuid=course_uuid)
# #             content = json.loads(request.body)
# #             if not content.get('message'):
# #                 return Response(status=status.HTTP_400_BAD_REQUEST)
# #             if not content.get('star_number'):
# #                 return Response(status=status.HTTP_400_BAD_REQUEST)
# #             serializer = CommentSerializer(data=content)
# #             if serializer.is_valid():
# #                 comment = serializer.save(user=request.user)
# #                 course.comments.add(comment)
# #                 return Response(status=status.HTTP_200_OK)

# #             else:
# #                 return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #         except:
# #             return Response(status=status.HTTP_400_BAD_REQUEST)


# # class UpdateCommentView(APIView):
# #     permission_classes = [permissions.IsAuthenticated]

# #     def put(self, request, comment_uuid, format=None):
# #         try:
# #             data = self.request.data
# #             user = request.user
# #             # answer_uuid = data["answer_uuid"]
# #             comment = get_object_or_404(Comment, uuid=comment_uuid)
# #             comment.message = data['message']
# #             comment.star_number = data['star_number']
# #             comment.save()

# #             return Response({'Success': 'Comment updated successfully.'})
# #         except:
# #             return Response({'Error': 'Something went wrong updating the comment'})


# # class DeleteCommentView(APIView):
# #     permission_classes = [permissions.IsAuthenticated]

# #     def post(self, request, comment_uuid, format=None):
# #         try:
# #             user = self.request.user
# #             data = self.request.data
# #             comment = get_object_or_404(Comment, uuid=comment_uuid)
# #             if not comment.user.email == user.email:
# #                 return Response({'Error': 'User can not delete this comment.'})

# #             delete_msg = data['delete_msg']
# #             if delete_msg:
# #                 comment.delete()

# #             return Response({'Success': 'Comment deleted successfully.'})
# #         except:
# #             return Response({'Error': 'Something went wrong deleting the comment'})
