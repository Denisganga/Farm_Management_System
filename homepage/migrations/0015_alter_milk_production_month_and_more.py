# Generated by Django 5.0 on 2024-01-05 21:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_alter_milk_production_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milk_production',
            name='Month',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='milk_production',
            name='Year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
