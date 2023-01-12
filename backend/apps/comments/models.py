from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4

from account.models import User


class Comment(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-date_created',)
