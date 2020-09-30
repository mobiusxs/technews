from django.urls import path

from . import views

app_name = 'vote'

urlpatterns = [
    path('comment/', views.CommentVoteView.as_view(), name='comment'),
    path('thread/', views.ThreadVoteView.as_view(), name='thread'),
]
