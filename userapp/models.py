from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy, ugettext_lazy


# Create your models here.
# Custom User Manager
class UserManager(BaseUserManager):

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Field is Required!!!")
        if not username:
            raise ValueError("UserName Field is Required!!!")
        if not password:
            raise ValueError("Password Field is Required!!!")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Custom User
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('Email Field'), max_length=255, unique=True, blank=False)
    username = models.CharField(gettext_lazy("Username Field"), max_length=30, unique=True, blank=False)
    date_joined = models.DateTimeField(gettext_lazy("Date Joined Field"), auto_now_add=True)

    is_superuser = models.BooleanField(default=False, help_text="Designate the superuser status", verbose_name="Superuser Status")
    is_staff = models.BooleanField(default=False, help_text="Designate the staff status", verbose_name="Staff Status")
    is_active = models.BooleanField(default=True, help_text="Designate the active status", verbose_name="Active Status")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
