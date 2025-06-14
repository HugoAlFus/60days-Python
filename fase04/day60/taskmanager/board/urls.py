from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Página principal con lista de tareas
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]

