from django.core.exceptions import ValidationError


def validate_comma_separated(ingredients):
    error_message = 'Ingredients must be separated by comma'
    check = ingredients.split(',')
    if len(check) <= 1:
        raise ValidationError(error_message)
