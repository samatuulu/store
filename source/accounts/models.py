from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, default='customer')
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.username
