from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vote
from apps.votes.serializers import VoteSerializer


class VoteListView(APIView):
    permission_classes = [permissions.IsAdminUser,]

    def get(self, request, format=None):
        votes = Vote.objects.all()
        serialized_votes = VoteSerializer(votes, many=True)
        return Response(serialized_votes.data, status=status.HTTP_200_OK)


class CreateVoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = self.request.user
        data = request.data

        user_id = user.id
        answer_uuid = data['answer_uuid']
        answer_vote = data['answer_vote']

        vote = Vote(
            user=user_id,
            answer=answer_uuid,
            vote=answer_vote
        )
        vote.save()
        serialized_vote = VoteSerializer(vote)
        return Response(serialized_vote.data, status=status.HTTP_201_CREATED)


class UpdateVoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, vote_uuid, format=None):

        user = self.request.user
        data = request.data
        vote = get_object_or_404(Vote, uuid=vote_uuid)

        if not vote.user.uuid == user.uuid:
            return Response({'Error', 'User credentials do not match the question.'}, status=status.HTTP_400_BAD_REQUEST)

        answer_vote = data['vote']
        vote.vote = answer_vote
        vote.save()
        serialized_vote = VoteSerializer(vote)
        return Response(serialized_vote.data, status=status.HTTP_200_OK)