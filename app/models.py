from django.db import models

# Create your models here.


class singup(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    repeat_password = models.CharField(max_length=50, null=True)


class login(models.Model):
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
