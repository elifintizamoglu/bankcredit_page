# Generated by Django 4.1.5 on 2023-02-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_credit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
