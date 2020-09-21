from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse

from .forms import CommentForm
from .models import Link, Profile, Comment


class IndexView(ListView):
    template_name = 'index/links.html'
    model = Link
    paginate_by = 10


class ThreadView(DetailView):
    template_name = 'index/thread.html'
    model = Link

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(link__id=self.object.id)
        return context


class ProfileView(DetailView):
    template_name = 'index/profile.html'
    model = Profile

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        profile = get_object_or_404(Profile, user__username=username)
        return profile


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


class CommentFormView(FormView):
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.link = get_object_or_404(Link, id=self.request.POST['link-id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index:thread', kwargs={'pk': self.object.link.id})


class NewLinkListView(ListView):
    template_name = 'index/links.html'
    model = Link
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            return Link.objects.filter(author__username=username).order_by('-created')
        return Link.objects.all().order_by('-created')


class NewCommentListView(ListView):
    template_name = 'index/comments.html'
    model = Comment
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            return Comment.objects.filter(author__username=username).order_by('-created')
        return Comment.objects.all().order_by('-created')
