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

def Add_employees(request):
    if request.method=='POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            employees= form.save(commit=False)
            employees.user = request.user

            form.save()

            return redirect('homepage:show-employees')
        
    else:
        form =EmployeesForm()
    return render(request, 'homepage/addemployees.html', {'form':form})