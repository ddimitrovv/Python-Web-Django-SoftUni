from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )
    age = models.PositiveIntegerField()
    image = models.URLField()


class Note(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    image = models.URLField()
    content = models.TextField()
