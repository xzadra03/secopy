from django.urls import path
from . import views

#url conf
urlpatterns = [
    path('', views.intro),
    path('login/', views.auth_login),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('results/', views.results),
    path('results/logout/', views.logout_user)
]