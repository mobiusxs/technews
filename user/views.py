from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import User


class UserDetailView(DetailView):
    template_name = 'user/user.html'
    model = User

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)


@login_required
def update_about_view(request):
    user = User.objects.get(username=request.user.username)
    user.about = request.POST.get('about')
    user.save()
    return HttpResponseRedirect(reverse('user:detail', kwargs={'username': request.user.username}))
