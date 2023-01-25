from django.contrib import admin

from djangoProject.departments.models import Departments


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    pass
