from django.contrib import admin

from models_exercise.employees.models import Employee


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    search_fields = ['first_name']
    fields = [('first_name', 'last_name'), 'job_level']
    pass
