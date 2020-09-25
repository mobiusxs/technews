from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import Link, Profile, Comment


ORDERING = {
    'new': '-created',
    'top': 'karma',
}


class LinkListView(ListView):
    template_name = 'index/links.html'
    model = Link
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('u')
        # Use default if o=None or invalid
        ordering = ORDERING.get(self.request.GET.get('o', ''), '-created')
        if username:
            queryset = Link.objects.filter(author__username=username).annotate(comment_count=Count('comment')).order_by(ordering)
            return queryset
        else:
            return Link.objects.annotate(comment_count=Count('comment')).order_by(ordering)


class LinkDetailView(DetailView):
    template_name = 'index/link.html'
    model = Link

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(link__id=self.object.id)
        return context


class LinkDeleteView(DeleteView):
    model = Link
    success_url = '/'
    template_name = 'index/confirm_delete.html'
    template_name_suffix = ''

    def get_queryset(self):
        return Link.objects.annotate(comment_count=Count('comment'))


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
        return reverse('index:link', kwargs={'pk': self.object.id})


class CommentFormView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.link = get_object_or_404(Link, id=self.request.POST['link-id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index:link', kwargs={'pk': self.object.link.id})


class CommentListView(ListView):
    template_name = 'index/comments.html'
    model = Comment
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('u')
        # Use default if o=None or invalid
        ordering = ORDERING.get(self.request.GET.get('o', ''), '-created')
        if username:
            return Comment.objects.filter(author__username=username).order_by(ordering)
        else:
            return Comment.objects.all().order_by(ordering)


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['text']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('index:link', kwargs={'pk': self.object.link.id})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'index/confirm_delete.html'
    template_name_suffix = ''

    def get_success_url(self):
        return reverse('index:link', kwargs={'pk': self.object.link.id})


@login_required
def update_about(request):
    p = Profile.objects.get(user__username=request.user.username)
    p.about = request.POST.get('about')
    p.save()
    return HttpResponseRedirect(reverse('index:profile', kwargs={'username': request.user.username}))
