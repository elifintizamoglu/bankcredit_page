# Generated by Django 4.1.5 on 2023-03-06 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0023_rename_bank_bank_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank_option',
            old_name='bank_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bank_option',
            old_name='bank_slug',
            new_name='slug',
        ),
    ]