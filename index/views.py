from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

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


class SubmitView(LoginRequiredMixin, CreateView):
    template_name = 'index/submit.html'
    model = Link
    fields = ['url', 'text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index:thread', kwargs={'pk': self.object.id})
