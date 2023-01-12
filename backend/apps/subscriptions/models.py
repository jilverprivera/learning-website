from django.db import models

from uuid import uuid4

from account.models import User
from apps.pricing.models import Pricing

PRICING_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('active', 'Active'),
    ('trialing', 'Trialing')
)


class Subscription(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=PRICING_STATUS_CHOICES, default='pending')
    stripe_subscription_id = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"
