from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path("register", views.register_user, name="register")
]