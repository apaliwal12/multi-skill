# Generated by Django 3.0.7 on 2020-06-17 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminview', '0002_auto_20200617_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='skills',
            new_name='skill',
        ),
    ]
