from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact_form_sent')
    template_name = 'pages/contact.html'
