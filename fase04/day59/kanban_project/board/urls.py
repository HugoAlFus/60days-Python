from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_view, name='kanban_board'),
    path('update/', views.update_task_status, name='update_task_status'),
]
