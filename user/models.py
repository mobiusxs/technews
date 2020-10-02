from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    about = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def thread_karma(self):
        return User.objects.filter(id=self.id).aggregate(thread_karma=models.Sum('thread__threadvote__value'))['thread_karma']

    @property
    def comment_karma(self):
        return User.objects.filter(id=self.id).aggregate(comment_karma=models.Sum('comment__commentvote__value'))['comment_karma']

    @property
    def karma(self):
        return self.thread_karma + self.comment_karma
