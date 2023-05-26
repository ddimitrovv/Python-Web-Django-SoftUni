from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from Custom_validators.custom_validators import isalnum_and_underscore


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            MaxLengthValidator(USERNAME_MAX_LEN),
            isalnum_and_underscore,
        ),
        blank=False,
        null=False,
        verbose_name='Username',
    )

    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name='Email',
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Age',
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0

    class GenreTypes(models.TextChoices):
        POP_MUSIC = "Pop Music",
        JAZZ_MUSIC = "Jazz Music",
        RNB_MUSIC = "R&B Music",
        ROCK_MUSIC = "Rock Music",
        COUNTRY_MUSIC = "Country Music",
        DANCE_MUSIC = "Dance Music",
        HIP_HOP_MUSIC = "Hip Hop Music",
        OTHER = "Other"

    name = models.CharField(
        unique=True,
        validators=(
            MaxLengthValidator(ALBUM_NAME_MAX_LEN),
        ),
        blank=False,
        null=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        validators=(
            MaxLengthValidator(ARTIST_MAX_LEN),
        ),
        blank=False,
        null=False,
        verbose_name='Artist',
    )

    genre = models.CharField(
        validators=(
            MaxLengthValidator(GENRE_MAX_LEN),
        ),
        choices=GenreTypes.choices,
        blank=False,
        null=False,
        verbose_name='Genre',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description'
    )

    image = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
        blank=False,
        null=False,
        verbose_name='Price'
    )

