# Generated by Django 4.1.5 on 2023-02-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_credit_loan_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='slug',
            field=models.CharField(default='credittype', max_length=80),
        ),
    ]
