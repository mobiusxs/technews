from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    about = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def thread_karma(self):
        k = User.objects.filter(id=self.id).aggregate(k=models.Sum('thread__threadvote__value'))['k']
        return 0 if not k else k

    @property
    def comment_karma(self):
        k = User.objects.filter(id=self.id).aggregate(k=models.Sum('comment__commentvote__value'))['k']
        return 0 if not k else k

    @property
    def karma(self):
        return self.thread_karma + self.comment_karma
