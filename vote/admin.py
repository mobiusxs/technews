from django.contrib import admin

from .models import CommentVote, ThreadVote

admin.site.register(CommentVote)
admin.site.register(ThreadVote)
