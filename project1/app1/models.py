from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
edept=[
    ('Hr','HR'),
    ('Marketing', 'Marketing'),
    ('Finance', 'Finance'),
    ('Sales', 'Sales')
]

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    egender = models.CharField(max_length=150)
    eadd = models.CharField(max_length=200)
    edept = models.CharField(max_length=100, choices=edept)
    emobile =  PhoneNumberField()
    esal = models.FloatField()
    eskills = models.CharField(max_length=100)




    '''
!----  {% if user.is_authenticated %}
        <li class="nav-item"><a class="nav-link" href="#"><span>Hello..<b>{{user.username}}</b></span>LOGOUT</a></li>
        {% else %}
        <li class="nav-item"><a  class="nav-link" href="#">LOGIN</a></li>
        <li class="nav-item"><a  class="nav-link" href="#">REGISTER </a></li> 
        {% endif %} -->

    '''
