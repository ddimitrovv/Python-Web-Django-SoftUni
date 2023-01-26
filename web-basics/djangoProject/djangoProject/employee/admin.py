from django.contrib import admin

from djangoProject.employee.models import Employee


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    pass
