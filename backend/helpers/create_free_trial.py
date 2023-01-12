from account.models import User

from apps.courses.models import Pricing
from apps.courses.models import Subscription

import stripe


def create_free_trial(request, user):

    user = User.objects.get(email=user.email)
    if not user.is_superuser:
        free_trial_pricing = Pricing.objects.get(name='Free Trial')

        subscription = Subscription.objects.create(
            user=user,
            pricing=free_trial_pricing
        )

        stripe_customer = stripe.Customer.create(
            email=user.email
        )

        stripe_subscription = stripe.Subscription.create(
            customer=stripe_customer["id"],
            items=[{'price': 'price_1HAFmwA2yg3TLgLvda4AwmQb'}],
            trial_period_days=3
        )

        subscription.status = stripe_subscription["status"]
        subscription.stripe_subscription_id = stripe_subscription["id"]
        subscription.save()
        user.stripe_customer_id = stripe_customer["id"]

        user.save()
