from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse

from comment.models import Comment
from comment.forms import CommentCreateForm
from .models import Thread


ORDERING = {
    'new': '-datetime',
    'top': 'karma',
}


class ThreadListView(ListView):
    template_name = 'thread/list.html'
    model = Thread
    paginate_by = 10

    def get_queryset(self):
        """Multipurpose overwrite:
        1. Allow fetching of user-specific link feeds.
        2. Annotate the comment counts for each link
        3. Annotate the total karma value for each link
        4. Apply ordering
        """

        username = self.request.GET.get('u')
        # Use default if o=None or invalid
        ordering = ORDERING.get(self.request.GET.get('o', ''), '-datetime')

        if username:  # filter for specific users
            queryset = Thread.objects.filter(user__username=username).annotate(comment_count=Count('comment')).annotate(karma=Sum('threadvote__value')).order_by(ordering)
            return queryset
        else:
            return Thread.objects.annotate(comment_count=Count('comment')).annotate(karma=Sum('threadvote__value')).order_by(ordering)


class ThreadDetailView(DetailView):
    template_name = 'thread/detail.html'
    model = Thread

    def get_queryset(self):
        return Thread.objects.annotate(comment_count=Count('comment')).annotate(karma=Sum('threadvote__value'))

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()
        context['comments'] = Comment.objects.filter(thread__id=self.object.id)
        return context


class ThreadDeleteView(LoginRequiredMixin, DeleteView):
    model = Thread
    success_url = '/'
    template_name = 'thread/delete.html'
    template_name_suffix = ''

    def get_queryset(self):
        return Thread.objects.annotate(comment_count=Count('comment')).annotate(karma=Sum('threadvote__value'))


class ThreadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'thread/create.html'
    model = Thread
    fields = ['url', 'text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thread:detail', kwargs={'pk': self.object.id})
