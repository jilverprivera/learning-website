from django.db import models
import uuid
from account.models import User


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('created_at',)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True, default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        if not self.slug:
            slug_generated = self.name.lower().split(' ')
            self.slug = "-".join(slug_generated)
            self.save()
            return slug_generated
        else:
            return self.slug

    def get_subcategories(self):
        return SubCategory.objects.filter(category=self).all()


class SubCategory(models.Model):

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ('created_at',)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True)
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        if not self.slug:
            slug_generated = self.name.lower().split(' ')
            self.slug = "-".join(slug_generated)
            self.save()
            return slug_generated
        else:
            return self.slug