from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


from helpers.countries import Countries


def user_directory_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.title, filename)


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            ** extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("User must have is_staff = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("User must have is_superuser = True.")
        return self._create_user(email, password, first_name, last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    image = models.ImageField(upload_to=user_directory_path, default="user/default_image.jpeg", blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=128, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address_line_1 = models.CharField(max_length=255, default='', null=True)
    address_line_2 = models.CharField(max_length=255, default='', null=True)
    city = models.CharField(max_length=128, default='', null=True)
    province_region = models.CharField(max_length=128, default='', null=True)
    zipcode = models.CharField(max_length=32, default='', null=True)
    phone = models.CharField(max_length=64, default='', null=True)
    country_region = models.CharField(max_length=64, choices=Countries.choices, default=Countries.Colombia)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-email',)

    def __str__(self):
        return self.email

    def get_image(self):
        return self.image.url
