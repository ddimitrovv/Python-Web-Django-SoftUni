# Generated by Django 4.2.1 on 2023-05-25 09:24

import custom_validators.custom_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Indoor Plants', 'Indoor'), ('Outdoor Plants', 'Outdoor')], max_length=20, verbose_name='Plant Type')),
                ('name', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(20), custom_validators.custom_validators.contains_only_letters], verbose_name='Name')),
                ('image', models.URLField(verbose_name='Image Url')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(validators=[custom_validators.custom_validators.starts_with_capital_letter, django.core.validators.MaxLengthValidator(20)], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(validators=[custom_validators.custom_validators.starts_with_capital_letter, django.core.validators.MaxLengthValidator(20)], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(10)], verbose_name='Username'),
        ),
    ]
