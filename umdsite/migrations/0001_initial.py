# Generated by Django 4.0.3 on 2022-04-07 01:44

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('full_name', models.CharField(max_length=15)),
                ('phone_no', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=6)),
                ('user_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pass_key', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_name', models.CharField(max_length=10)),
                ('vol_pass', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='request_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=15)),
                ('med_name', models.CharField(max_length=15)),
                ('user_address', models.CharField(max_length=30)),
                ('user_name', models.ForeignKey(on_delete=builtins.callable, to='umdsite.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='donate_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=15)),
                ('med_details', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=30)),
                ('user_name', models.ForeignKey(on_delete=builtins.callable, to='umdsite.user_registration')),
            ],
        ),
    ]
