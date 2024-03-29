# Generated by Django 5.0 on 2024-01-10 06:53

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_alter_milk_production_month_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eggs_production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('Month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('Day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('Poultry_number', models.IntegerField()),
                ('Morning_egg_collection', models.DecimalField(decimal_places=2, help_text='total number of eggs collected', max_digits=10)),
                ('Midday_egg_collection', models.DecimalField(blank=True, decimal_places=2, help_text='total number of eggs collected', max_digits=10)),
                ('Evening_egg_collection', models.DecimalField(blank=True, decimal_places=2, help_text='total number of eggs collected', max_digits=10)),
                ('Total_egg_collection', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('Morning_feeds', models.DecimalField(decimal_places=2, help_text='feed consumed in kg', max_digits=10)),
                ('Evening_feeds', models.DecimalField(blank=True, decimal_places=2, help_text='feed consumed in kg', max_digits=10)),
                ('Total_feeds', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('Comments', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
