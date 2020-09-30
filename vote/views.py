import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse

from .models import CommentVote, ThreadVote
from comment.models import Comment
from thread.models import Thread


class CommentVoteView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request):
        data = json.loads(request.body)
        vote_value = int(data['value'])
        comment = Comment.objects.get(id=data['id'])

        try:
            vote = CommentVote.objects.get(user=request.user, comment=comment)
        except CommentVote.DoesNotExist:
            vote = CommentVote(user=request.user, comment=comment, value=vote_value)
            vote.save()
        else:
            if vote.value != vote_value:
                vote.delete(keep_parents=True)
        return HttpResponse('')


class ThreadVoteView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request):
        data = json.loads(request.body)
        vote_value = int(data['value'])
        thread = Thread.objects.get(id=data['id'])

        try:
            vote = ThreadVote.objects.get(user=request.user, thread=thread)
        except ThreadVote.DoesNotExist:
            vote = ThreadVote(user=request.user, thread=thread, value=vote_value)
            vote.save()
        else:
            if vote.value != vote_value:
                vote.delete(keep_parents=True)
        return HttpResponse('')
