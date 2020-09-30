from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('create/', views.CommentCreateView.as_view(), name='create'),
    path('list', views.CommentListView.as_view(), name='list'),
    path('update/<int:pk>', views.CommentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CommentDeleteView.as_view(), name='delete'),
]
