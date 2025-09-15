from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Root page
    path('tasks/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
]
