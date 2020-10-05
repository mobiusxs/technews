from django.urls import path
from django.views.generic import TemplateView

from .views import ContactFormView

app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('contact_sent/', TemplateView.as_view(template_name='pages/contact_sent.html'), name='contact_sent'),
    path('privacy/', TemplateView.as_view(template_name='pages/privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
]
