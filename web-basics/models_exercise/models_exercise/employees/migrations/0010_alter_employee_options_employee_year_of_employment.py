# Generated by Django 4.1.6 on 2023-02-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_rename_emai_address_employee_email_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-year_of_employment']},
        ),
        migrations.AddField(
            model_name='employee',
            name='year_of_employment',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
    ]