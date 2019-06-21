from django.db import models

# Create your models here.
class Student(models.Model):
    login = models.CharField(verbose_name='Id', db_index=True, unique=True, max_length=32)
    firstname = models.CharField(verbose_name='Firstname',  max_length=64)
    lastname = models.CharField(verbose_name='Lastname', max_length=64)
    year = models.CharField(verbose_name='Year', max_length=4)
    phonenumber = models.CharField(verbose_name='Phone number', max_length=11)