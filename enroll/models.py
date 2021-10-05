from django.db import models
from django.forms import widgets
from django import forms

class Class(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=20)  
    class Meta:
     db_table="Class"
# Create your models here.
