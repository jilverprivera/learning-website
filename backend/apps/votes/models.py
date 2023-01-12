from django.db import models
from uuid import uuid4

from account.models import User
from apps.answers.models import Answer

VOTES_CHOICES = (
    ('Up', 'Up Vote'),
    ('Down', 'Down Vote'),
)


class Vote(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,)
    vote = models.CharField(choices=VOTES_CHOICES, max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
