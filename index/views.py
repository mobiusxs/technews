from django.views.generic import ListView, DetailView

from .models import Link, Profile


class IndexView(ListView):
    template_name = 'index/index.html'
    model = Link


class ThreadView(DetailView):
    template_name = 'index/thread.html'
    model = Link


class ProfileView(DetailView):
    template_name = 'index/profile.html'
    model = Profile
