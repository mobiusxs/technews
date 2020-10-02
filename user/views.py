from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import User


class UserDetailView(DetailView):
    template_name = 'user/user.html'
    model = User

    def get_object(self, queryset=None):
        """Enable lookups by username rather than pk"""

        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        """Enable displaying comment and thread karma totals on user profile view"""

        context = super().get_context_data(**kwargs)
        context['thread_karma'] = User.objects.filter(id=self.object.id).aggregate(comment_karma=Sum('comment__commentvote__value'))['comment_karma']
        context['comment_karma'] = User.objects.filter(id=self.object.id).aggregate(thread_karma=Sum('thread__threadvote__value'))['thread_karma']
        return context


@login_required
def update_about_view(request):
    """Allow users to update their 'about' blurb on profile view"""

    user = User.objects.get(username=request.user.username)
    user.about = request.POST.get('about')
    user.save()
    return HttpResponseRedirect(reverse('user:detail', kwargs={'username': request.user.username}))
