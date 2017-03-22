from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    follows = models.ManyToManyField('self', related_name='follows', symmetrical=False)