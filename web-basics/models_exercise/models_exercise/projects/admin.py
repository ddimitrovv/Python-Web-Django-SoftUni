from django.contrib import admin

from models_exercise.projects.models import Projects


@admin.register(Projects)
class AdminProjects(admin.ModelAdmin):
    pass
