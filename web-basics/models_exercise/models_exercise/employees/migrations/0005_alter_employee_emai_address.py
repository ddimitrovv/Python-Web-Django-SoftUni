# Generated by Django 4.1.6 on 2023-02-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_month_of_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emai_address',
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
    ]