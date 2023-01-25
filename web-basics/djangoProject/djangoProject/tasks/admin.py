from django.contrib import admin

from djangoProject.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
