from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    emai_address = models.EmailField(unique=True)
    works_full_time = models.BooleanField(default=True)
    job_level = models.CharField(
        max_length=20,
        default='Junior'
    )
    photo = models.URLField(blank=True)
    birth_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job_level}'
