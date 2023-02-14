import re

from django.core.exceptions import ValidationError


def comma_separated(ingredients):
    check = re.findall("[a-zA-Z]+", ingredients)
    if len([x for x in ingredients.split(',')]) != len(check):
        raise ValidationError(
            'Ingredients must be separated by comma!',
            params={'ingredients': ingredients},
        )
