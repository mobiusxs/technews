from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('submit/', views.SubmitView.as_view(), name='submit'),
    path('comment/', views.CommentFormView.as_view(), name='comment'),
    path('newlinks/', views.NewLinkListView.as_view(), name='newlinks'),
    path('newcomments/', views.NewCommentListView.as_view(), name='newcomments'),
    path('thread/<int:pk>', views.ThreadView.as_view(), name='thread'),
    path('profile/<str:username>', views.ProfileView.as_view(), name='profile'),
]
