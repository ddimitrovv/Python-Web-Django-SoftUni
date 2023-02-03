from django.db import models


class Departments(models.Model):
    department_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.department_name}'
