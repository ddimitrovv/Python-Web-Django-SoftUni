from django.core.validators import MaxLengthValidator
from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENTS_MAX_LEN = 250

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Title',
    )

    image = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    description = models.CharField(
        blank=False,
        null=False,
        verbose_name='Description',
    )

    ingredients = models.TextField(
        max_length=INGREDIENTS_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Ingredients',
    )

    time_to_prepare = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name='Time',
    )

    def __str__(self):
        return self.title
