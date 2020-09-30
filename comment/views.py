from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from django.urls import reverse

from .forms import CommentCreateForm
from .models import Comment
from thread.models import Thread


ORDERING = {
    'new': '-datetime',
    'top': 'karma',
}


class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.thread = get_object_or_404(Thread, id=self.request.POST['thread-id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thread:detail', kwargs={'pk': self.object.thread.id})


class CommentListView(ListView):
    template_name = 'comment/list.html'
    model = Comment
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('u')
        # Use default if o=None or invalid
        ordering = ORDERING.get(self.request.GET.get('o', ''), '-datetime')
        if username:
            return Comment.objects.filter(user__username=username).order_by(ordering)
        else:
            return Comment.objects.all().order_by(ordering)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/update.html'
    template_name_suffix = ''

    def get_success_url(self):
        return reverse('thread:detail', kwargs={'pk': self.object.thread.id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/delete.html'
    template_name_suffix = ''

    def get_success_url(self):
        return reverse('thread:detail', kwargs={'pk': self.object.thread.id})
