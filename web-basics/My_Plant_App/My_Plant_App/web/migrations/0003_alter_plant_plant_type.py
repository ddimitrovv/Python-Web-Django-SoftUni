# Generated by Django 4.2.1 on 2023-05-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_plant_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('Indoor Plants', 'Indoor Plants'), ('Outdoor Plants', 'Outdoor Plants')], max_length=20, verbose_name='Plant Type'),
        ),
    ]