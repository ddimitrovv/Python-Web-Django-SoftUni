from django.db import models

from project_validators.custom_validators import comma_separated


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250, validators=[comma_separated])
    time = models.IntegerField()

    def __str__(self):
        return self.title
