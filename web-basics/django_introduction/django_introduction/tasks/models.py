from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()

