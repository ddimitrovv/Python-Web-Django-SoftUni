from django.contrib import admin

from models_exercise.appointments.models import ProjectAppointment


@admin.register(ProjectAppointment)
class AdminProjectAppointment(admin.ModelAdmin):
    pass
