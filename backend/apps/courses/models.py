from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid
from mutagen.mp4 import MP4,MP4StreamInfoError
from decimal import Decimal

from account.models import User
from apps.category.models import SubCategory

from helpers.get_timer import get_timer
from helpers.validate_video import validate_video



def course_thumbnail_directory_path(instance, filename):
    return 'courses/{0}/{1}'.format(instance.author.uuid, filename)


def course_sale_video_path(instance, filename):
    return 'courses/{0}/sale_video/{1}'.format(instance.author.uuid,filename)


def course_resources_path(instance, filename):
    return 'courses/{0}/resources/{1}'.format(instance.user.uuid, filename)


def course_lessons_path(instance, filename):
    return 'courses/{0}/lessons/{1}/{2}'.format(instance.user.uuid, instance.episode_number, filename)


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

PAYMENT_CHOICES = (
    ('paid', 'Paid'),
    ('free', 'Free'),
)

VOTES_CHOICES = (
    ('Up', 'Up Vote'),
    ('Down', 'Down Vote'),
)

PRICING_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('active', 'Active'),
    ('trialing', 'Trialing')
)


class Course(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=course_thumbnail_directory_path, null=True, blank=True)
    sale_video = models.FileField(upload_to=course_sale_video_path, null=False, blank=True)
    course_type = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='paid')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    sold = models.IntegerField(default=0, blank=True)
    course_length = models.CharField(default=0, max_length=64)
    best_seller = models.BooleanField(default=False)
    total_stars = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    pricing_tiers = models.ManyToManyField("pricing.Pricing", blank=True)
    # what_learnt = models.ManyToManyField('WhatLearnt', blank=True)
    requisite = models.ManyToManyField('requisites.Requisite', blank=True)
    sections = models.ManyToManyField('sections.Section', blank=True)
    resources = models.ManyToManyField('resources.Resource', blank=True)
    comments = models.ManyToManyField('comments.Comment', blank=True, related_name='comments')

    publication_date = models.DateTimeField(default=timezone.now)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager() 
    postobjects = PostObjects()

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return self.title

    def get_sale_video(self):
        if self.thumbnail:
            return self.sale_video.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    def get_stars(self):
        comments = self.comments.all()
        star = 0
        for comment in comments:
            star += comment.star_number
        try:
            star /= len(comments)
        except ZeroDivisionError:
            star = 0
        return star

    def get_number_starts(self):
        self.total_stars = len(self.comments.all())
        self.save()
        return len(self.comments.all())

    def get_total_lectures(self):
        lectures=0
        for section in self.sections.all():
            lectures+=len(section.episodes.all())
        return lectures

    def total_course_length(self):
        length=Decimal(0.00)
        for section in self.sections.all():
            for episode in section.episodes.all():
                length +=episode.length
        self.course_length = length
        self.save()
        return get_timer(length)





# class WhatLearnt(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title



class CoursesLibrary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    class Meta:
        verbose_name_plural = "Bookmarked Courses Library"

    def __str__(self):
        return self.author.email


class PaidCoursesLibrary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    class Meta:
        verbose_name_plural = "Purchased Courses Library"

    def __str__(self):
        return self.author.email
