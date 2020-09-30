from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
    path('update/', views.update_about_view, name='update'),
]
