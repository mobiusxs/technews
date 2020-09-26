from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from index.models import Comment, Link

VOTES = [
    (1, 1),
    (-1, -1),
]


class LinkVote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    content_object = models.ForeignKey(Link, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VOTES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['content_object', 'voter'], name='link_voter')
        ]


class CommentVote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    content_object = models.ForeignKey(Comment, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VOTES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['content_object', 'voter'], name='comment_voter')
        ]
