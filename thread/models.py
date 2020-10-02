from django.db import models

from user.models import User


class Thread(models.Model):
    """Simple temporary Thread model.
    Supports only links for now.
    """

    url = models.URLField()
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f'[{self.user.username}] {self.text}'

    @property
    def karma(self):
        return Thread.objects.filter(id=self.id).aggregate(thread_karma=models.Sum('threadvote__value'))['thread_karma']

    @property
    def comment_count(self):
        return Thread.objects.filter(id=self.id).aggregate(comment_count=models.Count('comment__id'))['comment_count']
