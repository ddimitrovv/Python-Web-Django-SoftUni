from django.core.exceptions import ValidationError


def starts_with_capital_letter(word):
    error_message = 'Your name must start with a capital letter!'
    if word[0] != word[0].upper():
        raise ValidationError(error_message)
    return word


def contains_only_letters(word):
    error_message = 'Plant name should contain only letters!'
    for letter in word:
        if not letter.isalpha():
            raise ValidationError(error_message)
