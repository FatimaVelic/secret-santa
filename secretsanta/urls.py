from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('participants/', views.ParticipantsListView.as_view(), name ='participants'),
    path('register/', views.register_user, name='register'),
    path('match-pairs/', views.matchPairs, name='match'),
]