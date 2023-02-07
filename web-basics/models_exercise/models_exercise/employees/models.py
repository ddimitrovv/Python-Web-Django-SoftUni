from django.db import models

from models_exercise.departments.models import Departments
from models_exercise.projects.models import Projects


class Employee(models.Model):

    MONTHS = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'Aril'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(
        unique=True,
        editable=False,
    )
    works_full_time = models.BooleanField(default=True)
    month_of_employment = models.CharField(
        max_length=3,
        choices=MONTHS,
    )
    job_level = models.CharField(
        max_length=20,
        default='Junior',
    )
    photo = models.URLField(blank=True)
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE,
    )

    year_of_employment = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Employees'
        ordering = ['first_name', '-year_of_employment']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job_level} - {self.department}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
