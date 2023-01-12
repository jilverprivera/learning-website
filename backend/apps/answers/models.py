from django.db import models
from uuid import uuid4

from account.models import User
from apps.questions.models import Question
from apps.votes.models import Vote


class Answer(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.ForeignKey(Vote, on_delete=models.CASCADE)
    message = models.TextField()
    is_accepted_answer = models.BooleanField(default=False)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_positive_votes(self):
        up_votes = Vote.objects.filter(answer=self, vote='Up').count()
        self.positive_votes = up_votes
        self.save()
        return self.positive_votes

    def get_negative_votes(self):
        down_votes = Vote.objects.filter(answer=self, vote='Down').count()
        self.negative_votes = down_votes
        self.save()
        return self.negative_votes

    def get_votes(self):
        up_votes = Vote.objects.filter(answer=self, vote='Up').count()
        down_votes = Vote.objects.filter(answer=self, vote='Down').count()
        self.votes = up_votes - down_votes
        self.save()
        return self.votes
