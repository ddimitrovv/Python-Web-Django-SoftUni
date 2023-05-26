from django.core.exceptions import ValidationError


def isalnum_and_underscore(word):
    error_message = 'Ensure this value contains only letters, numbers, and underscore.'
    for ch in word:
        if not ch.isalnum() and ch != '_':
            raise ValidationError(error_message)
    return word
