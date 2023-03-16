# Generated by Django 4.1.5 on 2023-03-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0027_remove_bankoption_credit_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='identification_number',
            field=models.CharField(error_messages={'unique': 'This identification number has been already registered!'}, max_length=11, unique=True),
        ),
    ]
