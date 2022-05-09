from dataclasses import fields
from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels = {
            'eid':'EMPLOYEE ID',
            'ename':'EMPLOYEE NAME',
            'egender': 'GENDER',
            'eadd': 'ADDRESS',
            'edept':'DEPARTMENT',
            'emobile':'MOBILE NO:',
            'esal':'Salary',
            'eskills': 'SKILLS'
        }

        widgets ={
            'eid':forms.NumberInput(attrs={
                'palceholder':'111',
                'autocomplete':'off'
            }),

            'ename':forms.TextInput(attrs={
                'placeholder':'Enter Employee Name'
            })
        }