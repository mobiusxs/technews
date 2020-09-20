from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    karma = models.IntegerField(default=1)
    about = models.TextField(max_length=1000)

    def __str__(self):
        return self.user.username


class Link(models.Model):
    """Simple temporary Link model.
    Supports only links for now.

    Change to Thread model to support url and text threads.
    """
    url = models.URLField()
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.author.username}] {self.text}'


class Comment(models.Model):
    """Simple temporary Comment model.
    Supports on top-level comments for now.

    Use https://github.com/django-mptt/django-mptt to implement recursive nesting
    """

    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.author.username}] {self.created}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
