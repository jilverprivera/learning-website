from django.db import models
from uuid import uuid4

from account.models import User


class Requisite(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Requisite'
        verbose_name_plural = 'Requisites'
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
