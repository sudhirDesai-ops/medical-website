from django.db import models

# Create your models here.


class Sudhir(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

# class Login(models.Model):
#     email=models.EmailField()
#     password=models.IntegerField()



class login(models.Model):
    email=models.EmailField()
    password=models.IntegerField()



class account(models.Model):        
    email=models.EmailField()
    password=models.IntegerField()



class login2(models.Model):
    email=models.EmailField()
    password=models.IntegerField()

