# Generated by Django 4.2.1 on 2023-05-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('image', models.URLField(verbose_name='Image URL')),
                ('description', models.CharField(verbose_name='Description')),
                ('ingredients', models.TextField(max_length=250, verbose_name='Ingredients')),
                ('time_to_prepare', models.PositiveIntegerField(verbose_name='Time')),
            ],
        ),
    ]
