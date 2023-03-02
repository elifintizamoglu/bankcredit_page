# Generated by Django 4.1.5 on 2023-02-28 14:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_alter_credit_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('identification_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(11111111111), django.core.validators.MaxValueValidator(99999999999)])),
                ('credit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='credit.credit')),
            ],
        ),
    ]
