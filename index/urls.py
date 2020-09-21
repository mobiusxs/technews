from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.LinkListView.as_view(), name='index'),
    path('links/', views.LinkListView.as_view(), name='links'),
    path('link/<int:pk>', views.LinkDetailView.as_view(), name='link'),

    path('submit/', views.SubmitView.as_view(), name='submit'),
    path('comment/', views.CommentFormView.as_view(), name='comment'),
    path('newcomments/', views.NewCommentListView.as_view(), name='newcomments'),
    path('profile/<str:username>', views.ProfileView.as_view(), name='profile'),
]
