from django.shortcuts import render,redirect

# Create your views here.
def Mainpage(request):

    return render(request, 'homepage/home.html')

#views for the employees
from .employees_form import EmployeesForm
from .models import Employees

def Show_employees(request):
    employees = Employees.objects.filter(user=request.user)


    return render(request, 'homepage/showemployees.html', {'employees':employees})