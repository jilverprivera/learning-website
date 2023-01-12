# from django.core.cache import cache
# import json

# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from rest_framework.response import Response


# from apps.courses.models import Lesson
# from apps.courses.api.serializers.AnswerQuestionSerializer import *


# class ResponsePagination(PageNumberPagination):
#     page_query_param = 'p'
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 5


# class QuestionsView(APIView):
#     def get(self, request, lesson_uuid, *args, **kwargs):

#         if cache.get(lesson_uuid):
#             lesson = cache.get(lesson_uuid)
#         else:
#             lesson = Lesson.objects.get(uuid=lesson_uuid)
#             cache.set(lesson_uuid, lesson)

#         paginator = ResponsePagination()
#         questions = lesson.questions.all()
#         questions = paginator.paginate_queryset(questions, request)
#         serialized_questions = QuestionSerializer(questions, many=True)

#         return paginator.get_paginated_response(serialized_questions.data)


# class QuestionView(APIView):
#     def get(self, request, question_uuid, *args, **kwargs):

#         if not Question.objects.all().filter(uuid=question_uuid).exists():
#             return Response({'Error', 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

#         question = Question.objects.get(uuid=question_uuid)
#         serialized_question = QuestionSerializer(question)
#         return Response(serialized_question.data, status=status.HTTP_200_OK)


# class CreateQuestionView(APIView):
#     def post(self, request, lesson_uuid, *args, **kwargs):
#         if not Lesson.objects.all().filter(uuid=lesson_uuid).exists():
#             return Response({'Lesson with uuid: {0} does not exists.'.format(lesson_uuid)}, status=status.HTTP_404_NOT_FOUND)

#         data = self.request.data
#         user = data['user']
#         title = data['title']
#         message = data['message']
#         accepted_answer = data['accepted_answer']

#         if not user:
#             return Response({'User is required.'}, status=status.HTTP_400_NOT_FOUND)
#         if not title:
#             return Response({'Title is required.'}, status=status.HTTP_400_NOT_FOUND)
#         if not message:
#             return Response({'Message is required.'}, status=status.HTTP_400_NOT_FOUND)
#         if accepted_answer == 'false':
#             accepted_answer = bool(False)
#         else:
#             accepted_answer = bool(True)
#             # def post(self, request, lesson_uuid * args, **kwargs):
#             # if not Lesson.objects.all().filter(uuid=lesson_uuid).exists():
