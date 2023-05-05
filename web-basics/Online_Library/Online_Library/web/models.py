from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        blank=False,
        null=False,
    )
    image = models.URLField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    TITLE_MAX_LEN = 30
    TYPE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    image = models.URLField(
        blank=False,
        null=False,
    )
    book_type = models.CharField(
        max_length=TITLE_MAX_LEN,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.title}'

