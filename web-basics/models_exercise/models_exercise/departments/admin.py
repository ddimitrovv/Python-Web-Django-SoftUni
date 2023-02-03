from django.contrib import admin

from models_exercise.departments.models import Departments


@admin.register(Departments)
class AdminDepartments(admin.ModelAdmin):
    pass
