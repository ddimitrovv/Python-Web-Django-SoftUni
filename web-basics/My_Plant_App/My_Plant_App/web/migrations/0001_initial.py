# Generated by Django 4.2.1 on 2023-05-25 08:51

import custom_validators.custom_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(10)])),
                ('first_name', models.CharField(validators=[custom_validators.custom_validators.starts_with_capital_letter, django.core.validators.MaxLengthValidator(20)])),
                ('last_name', models.CharField(validators=[custom_validators.custom_validators.starts_with_capital_letter, django.core.validators.MaxLengthValidator(20)])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
