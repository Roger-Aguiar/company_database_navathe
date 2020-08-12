# Name:         Roger Silva Santos Aguiar
# Function:     It contains all the views for employee model
# Initial date: August 11, 2020
# Last update:  August 11, 2020
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request
from .models import Employee

def employees(request):
    employees = Employee.objects.all()
    # employees = [Employee.fname, Employee.minit, Employee.lname, Employee.bdate, Employee.address, Employee.sex, Employee.salary, Employee.dno]
    template = loader.get_template('employees/employees.html')
    context = {'employees': employees, 'title': 'Employees'}
    return HttpResponse(template.render(context, request))
    # return render(request, 'employees/employees.html', context)