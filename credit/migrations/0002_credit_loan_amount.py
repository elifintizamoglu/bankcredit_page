# Generated by Django 4.1.5 on 2023-02-26 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='loan_amount',
            field=models.IntegerField(default=500000, validators=[django.core.validators.MinValueValidator(500000), django.core.validators.MaxValueValidator(6000000)]),
        ),
    ]
