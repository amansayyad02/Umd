# Generated by Django 4.0.3 on 2022-04-07 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umdsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='donate_medicine',
            new_name='donated_medicine',
        ),
        migrations.RenameModel(
            old_name='request_medicine',
            new_name='requested_medicine',
        ),
    ]
