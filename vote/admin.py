from django.contrib import admin

from .models import CommentVote, LinkVote

admin.site.register(CommentVote)
admin.site.register(LinkVote)
