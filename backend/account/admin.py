from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'uuid', 'stripe_customer_id', 'is_staff', 'is_superuser', 'country_region',)
    list_display_links = ('email', 'uuid')
    list_filter = ('email', 'uuid', 'stripe_customer_id')
    search_fields = ('email', 'uuid', 'stripe_customer_id', )
    list_per_page = 25


admin.site.register(User, UserAdmin)
