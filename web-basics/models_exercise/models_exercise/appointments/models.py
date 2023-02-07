from django.db import models

from models_exercise.employees.models import Employee
from models_exercise.projects.models import Projects


class ProjectAppointment(models.Model):

    class Meta:
        verbose_name_plural = 'Appointments'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    start_date = models.DateField()
    role = models.CharField(max_length=30)

    def __str__(self):
        return f'Project name: {self.project} || Employee: {self.employee} -> {self.role} || Start date: {self.start_date}'
