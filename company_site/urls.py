# Name:         Roger Silva Santos Aguiar
# Function:     All the views will be mapped here.
# Initial date: August 11, 2020
# Last update:  August 11, 2020

from django.urls import path
from . import views

app_name = 'company_site'

urlpatterns = [
    path('employees/', views.employees, name='employees')
]