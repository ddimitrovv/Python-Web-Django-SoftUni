from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    emai_address = models.EmailField()
    works_full_time = models.BooleanField()
    job_level = models.CharField(max_length=20)
    photo = models.URLField()
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job_level}'
    