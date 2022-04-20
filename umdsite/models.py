from tkinter import CASCADE
from typing import Callable
from django.db import models
from django.forms import EmailInput

# Create your models here.
class user_registration(models.Model):
    user_id=models.AutoField
    full_name=models.CharField(max_length=15)
    phone_no=models.CharField(max_length=10)
    city=models.CharField(max_length=15)
    pincode=models.CharField(max_length=6)
    user_name=models.CharField(max_length=10,primary_key=True)
    pass_key=models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

class user_login(models.Model):
    ul_id=models.AutoField
    ul_name=models.CharField(max_length=10)
    ul_pass=models.CharField(max_length=10)

    def __str__(self):
        return self.ul_name

class volunteer_login(models.Model):
    vol_id=models.AutoField
    vol_name=models.CharField(max_length=10)
    vol_pass=models.CharField(max_length=10)

    def __str__(self):
        return self.vol_name

class donated_medicine(models.Model):
    donate_med_id:models.AutoField
    user_name=models.CharField(max_length=10)
    med_name=models.CharField(max_length=15)
    med_details=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)

    def __str__(self):
        return self.med_name

class requested_medicine(models.Model):
    donate_med_id:models.AutoField
    user_name=models.CharField(max_length=10)
    full_name=models.CharField(max_length=15)
    med_name=models.CharField(max_length=15)
    user_address=models.CharField(max_length=30)

    def __str__(self):
        return self.med_name

class user_query(models.Model):
    query_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    query=models.CharField(max_length=50)

    def __str__(self):
        return self.query