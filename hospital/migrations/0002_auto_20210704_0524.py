# Generated by Django 3.2.4 on 2021-07-04 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='date1',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='time',
            new_name='time1',
        ),
    ]
