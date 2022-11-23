from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('register-administrator/', views.register_administrator, name='register-administrator'),
    path('register-employee/', views.register_employee, name='register-employee'),
    path('match-pairs/', views.match_pairs, name='match'),
    path('participants/', views.ParticipantsListView.as_view(), name='participants'),
    path('participants-delete/', TemplateView.as_view(template_name='participants_delete.html'), name='participants-delete'),
    path('participants-delete-completed/', TemplateView.as_view(template_name='participants_delete_completed.html'), name='delete-completed'),
    path('participants-reset/', views.participants_reset, name= 'participants-reset'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('participants-export/', views.exportSantasList, name='export'),
]