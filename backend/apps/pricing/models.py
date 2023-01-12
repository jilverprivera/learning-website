from django.db import models

from uuid import uuid4


class Pricing(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    stripe_price_id = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    currency = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'
        ordering = ('-uuid',)

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = self.name.lower().split(' ')
        if not self.slug:
            self.slug = "-".join(slug)
            self.save()
        return slug
