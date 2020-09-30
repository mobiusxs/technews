from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    karma = models.IntegerField(default=1)
    about = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username
