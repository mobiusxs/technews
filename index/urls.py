from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thread/<int:pk>', views.ThreadView.as_view(), name='thread'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile')
]
