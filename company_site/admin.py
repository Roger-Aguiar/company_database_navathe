# Name:         Roger Silva Santos Aguiar
# Function:     Admin settings
# Initial date: August 6, 2020
# Last update:  August 6, 2020

from django.contrib import admin
from .models import Employee

admin.site.register(Employee)