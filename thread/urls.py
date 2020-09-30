from django.urls import path

from . import views

app_name = 'thread'

urlpatterns = [
    path('list/', views.ThreadListView.as_view(), name='list'),
    path('create/', views.ThreadCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.ThreadDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.ThreadDeleteView.as_view(), name='delete'),
]
