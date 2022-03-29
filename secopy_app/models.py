#
# file: urls.py
# author: Jan Zádrapa, BUT FIT
# date: 3/2022
# brief: file, wher URL paths are set and view method is assigned to them
#
from django.db import models
from django.contrib.auth.models import User


class New_user(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=50)
    organisation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
