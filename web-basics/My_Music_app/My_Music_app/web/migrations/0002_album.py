# Generated by Django 4.2.1 on 2023-05-26 09:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, validators=[django.core.validators.MaxLengthValidator(30)], verbose_name='Album Name')),
                ('artist', models.CharField(validators=[django.core.validators.MaxLengthValidator(30)], verbose_name='Artist')),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R And B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], validators=[django.core.validators.MaxLengthValidator(30)], verbose_name='Genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Price')),
            ],
        ),
    ]
