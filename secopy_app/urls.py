#
# file: urls.py
# author: Jan Zádrapa, BUT FIT
# date: 3/2022
# brief: file where URL paths are set and view method is assigned to them
#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro),
    path('login/', views.auth_login),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('theory/', views.theory),
    path('test/', views.test),
    path('downloads/', views.download)
]