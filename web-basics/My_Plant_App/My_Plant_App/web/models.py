from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from custom_validators.custom_validators import starts_with_capital_letter, contains_only_letters


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            MaxLengthValidator(USERNAME_MAX_LEN)
        ),
        blank=False,
        null=False,
        verbose_name='Username',
    )

    first_name = models.CharField(
        validators=(
            starts_with_capital_letter,
            MaxLengthValidator(FIRST_NAME_MAX_LEN),
        ),
        blank=False,
        null=False,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        validators=(
            starts_with_capital_letter,
            MaxLengthValidator(FIRST_NAME_MAX_LEN),
        ),
        blank=False,
        null=False,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Plant(models.Model):
    PLANT_TYPE_MAX_LEN = 20
    PLANT_NAME_MAX_LEN = 20
    PLANT_NAME_MIN_LEN = 2

    class PlanTypeChoices(models.TextChoices):
        INDOOR_PLANTS = 'Indoor Plants',
        OUTDOOR_PLANTS = 'Outdoor Plants',

    plant_type = models.CharField(
        choices=PlanTypeChoices.choices,
        max_length=PLANT_TYPE_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Plant Type',
    )

    name = models.CharField(
        validators=(
            MinLengthValidator(PLANT_NAME_MIN_LEN),
            MaxLengthValidator(PLANT_NAME_MAX_LEN),
            contains_only_letters,
        ),
        blank=False,
        null=False,
        verbose_name='Name',
    )

    image = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image Url',
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='Description',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        verbose_name='Price',
    )

    def __str__(self):
        return self.name
