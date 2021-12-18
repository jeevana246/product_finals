from django.db import models

# Create your models here.
class administrator(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)

class scholar(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)
