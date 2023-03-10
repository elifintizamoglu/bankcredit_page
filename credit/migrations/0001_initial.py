# Generated by Django 4.1.5 on 2023-02-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('excerpt', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=500)),
                ('interest_rate', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
