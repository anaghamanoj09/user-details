from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.TextField()
    phone=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class image(models.Model):
    photo=models.FileField()

class country_tb(models.Model):
    c_name=models.CharField(max_length=20)

class state(models.Model):
    s_name=models.CharField(max_length=20)
    cid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
