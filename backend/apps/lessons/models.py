from django.db import models
from uuid import uuid4
from mutagen.mp4 import MP4, MP4StreamInfoError

from helpers.get_timer import get_timer

from account.models import User
from apps.sections.models import Section


def course_lessons_path(instance, filename):
    return 'courses/{0}/lessons/{1}/{2}'.format(instance.user.uuid, instance.episode_number, filename)


class Lesson(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=course_lessons_path)
    content = models.TextField()
    length = models.DecimalField(max_digits=100, decimal_places=2)
    resources = models.ManyToManyField('resources.Resource', blank=True)
    lesson_number = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ('lesson_number',)

    def __str__(self):
        return self.title

    def get_video_length(self):
        try:
            video = MP4(self.file)
            self.length = video.info.length
            self.save()
            return video.info.length
        except MP4StreamInfoError:
            return 0.0

    def get_video_length_time(self):
        return get_timer(self.length)

    def save(self, *args, **kwargs):
        self.length = self.get_video_length()
        return super().save(*args, **kwargs)
