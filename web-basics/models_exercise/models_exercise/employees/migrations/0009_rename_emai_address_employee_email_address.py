# Generated by Django 4.1.6 on 2023-02-07 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_employee_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emai_address',
            new_name='email_address',
        ),
    ]