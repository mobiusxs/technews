from django.contrib import admin

from .models import Link, Comment, Profile

admin.site.register(Profile)
admin.site.register(Link)
admin.site.register(Comment)
