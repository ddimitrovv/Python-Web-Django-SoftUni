from django.db import models


class Departments(models.Model):

    class Meta:
        verbose_name_plural = 'Departments'
    department_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.department_name}'
