from django.db import models
from uuid import uuid4

from account.models import User


def course_resources_path(instance, filename):
    return 'courses/{0}/resources/{1}'.format(instance.user.uuid, filename)


class Resource(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to=course_resources_path, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url
