# Generated by Django 4.1.5 on 2023-03-06 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0019_alter_bank_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='slug',
            new_name='bank_slug',
        ),
    ]
