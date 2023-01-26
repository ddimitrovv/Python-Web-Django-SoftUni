from django.db import models


class Employee(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    DEPARTMENT_MAX_LEN = 30

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN)
    department = models.CharField(max_length=DEPARTMENT_MAX_LEN)
    email = models.EmailField()
