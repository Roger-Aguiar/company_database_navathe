# Name:         Roger Silva Santos Aguiar
# Function:     Models for the company_navathe database
# Initial date: August 6, 2020
# Last update:  August 6, 2020

from django.db import models

class Employee(models.Model):
    fname = models.CharField('First name', max_length=15)
    minit = models.CharField('Initial second name', max_length=1, null=False)
    lname = models.CharField('Last name', max_length=15)
    ssn = models.CharField('Ssn', max_length=9, primary_key=True)
    bdate = models.DateTimeField('Birth date', null=False)
    address = models.CharField('Address', max_length=100, null=False)
    sex = models.CharField('Sex', max_length=1, null=False)
    salary = models.FloatField('Salary', null=False)
    dno = models.IntegerField('Dno')

    def __str__(self):
        employees = '{}   {}  {}   {}   {}   {}   {}   {}   {}' \
            .format(self.fname, self.minit, self.lname, self.ssn, str(self.bdate), self.address, self.sex, str(self.salary), str(self.dno))
        return employees