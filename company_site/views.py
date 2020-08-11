# Name:         Roger Silva Santos Aguiar
# Function:     It contains all the views for employee model
# Initial date: August 11, 2020
# Last update:  August 11, 2020
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request
from .models import Employee

def index():
    # employees = Employee.objects
    employees = [Employee.fname, Employee.minit, Employee.lname, Employee.ssn, Employee.bdate, Employee.address, Employee.sex, Employee.salary, Employee.dno]
    template = loader.get_template('company_site/index.html')
    context = {'employees': employees, 'title': 'Employees'}
    return HttpResponse(template.render(context, request))