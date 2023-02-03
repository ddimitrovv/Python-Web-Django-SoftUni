from django.db import models


class Projects(models.Model):
    MONTHS = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'Aril'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    ]

    project_name = models.CharField(max_length=30)
    start_month = models.CharField(
        max_length=3,
        choices=MONTHS,
    )
    end_month = models.CharField(
        max_length=3,
        choices=MONTHS,
    )

    def __str__(self):
        return f'{self.project_name} - {self.start_month} - {self.end_month}'
