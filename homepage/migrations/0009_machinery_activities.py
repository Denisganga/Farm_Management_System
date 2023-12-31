# Generated by Django 5.0 on 2023-12-29 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_crop_operations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery_activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_date', models.DateField(help_text='m/d/y')),
                ('Activity_type', models.CharField(max_length=20)),
                ('Activity_cost', models.IntegerField(blank=True)),
                ('Description', models.TextField(blank=True)),
                ('machinery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.machinery')),
            ],
        ),
    ]
