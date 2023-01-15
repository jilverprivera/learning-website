from django.db import models
from uuid import uuid4

from account.models import User


class Learning(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Learning'
        verbose_name_plural = 'Learnings'
        ordering = ('date_created',)
