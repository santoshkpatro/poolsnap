from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        if email is None:
            raise ValueError("Email must be provided!")

        if first_name is None:
            raise ValueError("First name must be provided")

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, **extra_fields)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        user = self.create_user(email, first_name, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    password_reset_required = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()
    active_objects = ActiveUserManager()

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email

    # Admin Panel
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
