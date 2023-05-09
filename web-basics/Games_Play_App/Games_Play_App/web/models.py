from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        blank=True,
        null=True,
    )

    picture = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15

    class CategoryChoices(models.TextChoices):
        ACTION = 'Action',
        ADVENTURE = 'Adventure',
        PUZZLE = 'Puzzle',
        STRATEGY = 'Strategy',
        SPORTS = 'Sports',
        BOARD_CARD_GAME = 'Board/Card Game',
        OTHER = 'Other'

    RATING_MIN = 0.1
    RATING_MAX = 5.0
    LEVEL_MIN = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        blank=False,
        null=False,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CategoryChoices.choices,
        blank=False,
        null=False
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX),
        ),
        blank=False,
        null=False
    )

    max_level = models.PositiveIntegerField(
        validators=(
            MinValueValidator(LEVEL_MIN),
        ),
        blank=True,
        null=True,
    )

    image = models.URLField(
        blank=False,
        null=False,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

