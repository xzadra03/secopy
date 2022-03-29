#file for registration of user model
#author: Django

from django.contrib import admin
from .models import New_user

#registration of model (table)
admin.site.register(New_user)