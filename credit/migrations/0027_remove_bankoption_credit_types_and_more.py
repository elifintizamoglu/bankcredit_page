# Generated by Django 4.1.5 on 2023-03-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0026_remove_bankoption_credit_types_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankoption',
            name='credit_types',
        ),
        migrations.AddField(
            model_name='bankoption',
            name='credit_types',
            field=models.ManyToManyField(to='credit.credit'),
        ),
    ]