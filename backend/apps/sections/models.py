from django.db import models
from decimal import Decimal
from uuid import uuid4

from account.models import User

from helpers import get_timer


class Section(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    section_number = models.IntegerField(blank=True, null=True)
    # lessons = models.ManyToManyField('lessons.Lesson', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('section_number',)

    def __str__(self):
        return self.title

    def total_length(self):
        total = Decimal(0.00)
        for lesson in self.lessons.all():
            total += lesson.length
        return get_timer(total, type='min')
