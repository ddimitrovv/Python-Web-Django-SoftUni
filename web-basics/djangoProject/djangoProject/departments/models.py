from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=30)
