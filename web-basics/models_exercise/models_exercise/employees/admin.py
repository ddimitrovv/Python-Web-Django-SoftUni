from django.contrib import admin

from models_exercise.employees.models import Employee


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    pass
