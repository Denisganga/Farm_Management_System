# Generated by Django 5.0 on 2023-12-26 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_livestock_production_production_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crops',
            name='Expenses',
        ),
        migrations.RemoveField(
            model_name='crops',
            name='Expenses_description',
        ),
    ]
