from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    phone_number = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class RoleChoices(models.TextChoices):
        ADMIN = 'Admin'
        USER = 'User'
        SUPER_USER = 'Super User'

    role = models.CharField(choices=RoleChoices.choices , default=RoleChoices.USER)