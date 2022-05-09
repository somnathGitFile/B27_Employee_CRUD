from urllib import request
from django.shortcuts import render, redirect
from .forms import Employeeform
from.models import Employee
# Create your views here.

def empformView(request):
    form = Employeeform()
    template_name = 'app1/empform.html'
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name, context)

def showempView(request):
    data = Employee.objects.all()
    template_name = 'app1/showemp.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updateEmpView(request, id):
    data = Employee.objects.get(id=id)
    form = Employeeform(instance=data)
    template_name = 'app1/empform.html'
    if request.method == 'POST':
        form = Employeeform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showemp_url')
    context = {'form': form}
    return render(request, template_name, context)

def deleteEmpView(request, id):
    data = Employee.objects.get(id=id)
    template_name = 'app1/confirmation.html'
    if request.method == 'POST':
        data.delete()
        return redirect('showemp_url')
    context = {'obj':data}
    return render(request, template_name, context)
