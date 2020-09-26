import json

from django.views.generic import View
from django.http import HttpResponse

from .models import CommentVote, LinkVote
from index.models import Link, Comment


class VoteView(View):
    http_method_names = ['post']

    def post(self, request):
        data = json.loads(request.body)
        vote_value = int(data['value'])
        if data['type'] == 'link':
            content_type = Link
            content_type_vote = LinkVote
        else:
            content_type = Comment
            content_type_vote = CommentVote
        content_object = content_type.objects.get(id=data['id'])

        try:
            vote = content_type_vote.objects.get(voter=request.user, content_object=content_object)
        except content_type_vote.DoesNotExist:
            vote = content_type_vote(voter=request.user, content_object=content_object, value=vote_value)
            vote.save()
        else:
            if vote.value != vote_value:
                vote.delete(keep_parents=True)
        return HttpResponse('')
