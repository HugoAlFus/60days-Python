from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('Por hacer', 'Por hacer'),
        ('En progreso', 'En progreso'),
        ('Hecho', 'Hecho'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_tasks')

    def __str__(self):
        return self.title
