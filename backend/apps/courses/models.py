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
    # resources = models.ManyToManyField('Resource', blank=True)
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


# # ---- PRICING ---- ✅ # 
# class Pricing(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     stripe_price_id = models.CharField(max_length=128)
#     name= models.CharField(max_length=64)
#     slug = models.SlugField(unique=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     currency = models.CharField(max_length=64)

#     def __str__(self):
#         return self.name

#     def get_slug(self):
#         slug = self.name.lower().split(' ')
#         if not self.slug:
#             self.slug = "-".join(slug)
#             self.save()
#         return slug


# # ---- SUBSCRIPTION ---- ✅ #
# class Subscription(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='pricing_subscriptions')
#     status = models.CharField(max_length=32, choices=PRICING_STATUS_CHOICES, default='pending')
#     stripe_subscription_id = models.CharField(max_length=128)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.user.email

#     @property
#     def is_active(self):
#         return self.status == "active" or self.status == "trialing"


# class WhatLearnt(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


# # class Requisite(models.Model):
# #     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=255)
# #     description = models.TextField()
# #     date_created = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.title


# class Section(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     section_number = models.IntegerField(blank=True, null=True)
#     lessons = models.ManyToManyField('Lesson', blank=True)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('section_number',)

#     def __str__(self):
#         return self.title

#     def total_length(self):
#         total = Decimal(0.00)
#         for lesson in self.lessons.all():
#             total += lesson.length
#         return get_timer(total, type='min')


# class Lesson(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to=course_lessons_path)
#     content = models.TextField()
#     length = models.DecimalField(max_digits=100, decimal_places=2)
#     resources = models.ManyToManyField('Resource', blank=True)
#     questions = models.ManyToManyField('Question', blank=True)
#     lesson_number = models.IntegerField(blank=True, null=True, default=0)

#     class Meta:
#         ordering = ('lesson_number',)

#     def __str__(self):
#         return self.title

#     def get_video_length(self):
#         try:
#             video = MP4(self.file)
#             return video.info.length
#         except MP4StreamInfoError:
#             return 0.0

#     def get_video_length_time(self):
#         return get_timer(self.length)

#     def save(self, *args, **kwargs):
#         self.length = self.get_video_length()
#         return super().save(*args, **kwargs)


# class Resource(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to=course_resources_path, blank=True, null=True)
#     url = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return self.file.url


# class Question(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     message = models.TextField()
#     accepted_answer = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_created',)

#     def __str__(self):
#         return self.title

#     def get_answers(self):
#         return Answer.objects.filter(question=self)

#     def get_answers_count(self):
#         return Answer.objects.filter(question=self).count()


# class Answer(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     message = models.TextField()
#     is_accepted_answer = models.BooleanField(default=False)
#     positive_votes = models.IntegerField(default=0)
#     negative_votes = models.IntegerField(default=0)
#     votes = models.IntegerField(default=0)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_created',)

#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name

#     def calculate_positive_votes(self):
#         up_votes = Vote.objects.filter(answer=self, vote='Up').count()
#         self.positive_votes = up_votes
#         self.save()
#         return self.positive_votes

#     def calculate_negative_votes(self):
#         down_votes = Vote.objects.filter(answer=self, vote='Down').count()
#         self.negative_votes = down_votes
#         self.save()
#         return self.negative_votes

#     def calculate_votes(self):
#         up_votes = Vote.objects.filter(answer=self, vote='Up').count()
#         down_votes = Vote.objects.filter(answer=self, vote='Down').count()
#         self.votes = up_votes - down_votes
#         self.save()
#         return self.votes


# class Vote(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_votes')
#     vote = models.CharField(choices=VOTES_CHOICES, max_length=4)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_created',)


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
