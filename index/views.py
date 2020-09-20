from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy, resolve, re_path

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


class SubmitView(CreateView):
    template_name = 'index/submit.html'
    model = Link
    fields = '__all__'

    def get_success_url(self):
        return reverse('index:thread', args=[self.object.id])
