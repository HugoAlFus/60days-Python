from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'user')
    search_fields = ('title',)
    list_filter = ('status', 'created_at')
