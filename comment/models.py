from django.db import models

from thread.models import Thread
from user.models import User


class Comment(models.Model):
    """Simple temporary Comment model.
    Supports only top-level comments for now.

    Use https://github.com/django-mptt/django-mptt to implement recursive nesting
    """

    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user.username}] {self.datetime}'
