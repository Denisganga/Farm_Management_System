from django.shortcuts import render, redirect


# Create your views here.
def Mainpage(request):
    return render(request, "homepage/home.html")


# views for the employees
from .employees_form import EmployeesForm
from .models import Employees


def Show_employees(request):
    employees = Employees.objects.filter(user=request.user)

    return render(request, "homepage/showemployees.html", {"employees": employees})


def Add_employees(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            employees = form.save(commit=False)
            employees.user = request.user

            form.save()

            return redirect("homepage:show-employees")

    else:
        form = EmployeesForm()
    return render(request, "homepage/addemployees.html", {"form": form})


def Delete_employees(request, Eid):
    employees = Employees.objects.get(Eid=Eid)
    if request.method == "POST":
        employees.delete()
        return redirect("homepage:show-employees")

    return render(request, "homepage/deleteemployees.html", {"employees": employees})


def Update_employees(request, Eid):
    employees = Employees.objects.get(Eid=Eid)
    form = EmployeesForm(request.POST, instance=employees)

    if form.is_valid():
        form.save()
        return redirect("homepage:show-employees")

    return render(request, "homepage/updateemployees.html", {"employees": employees})


# views for crops
from .models import Crops
from .crops_form import CropsForm


def Show_crops(request):
    crops = Crops.objects.filter(user=request.user)

    return render(request, "homepage/showcrops.html", {"crops": crops})


def Add_crops(request):
    if request.method == "POST":
        form = CropsForm(request.POST)
        if form.is_valid():
            crops = form.save(commit=False)
            crops.user = request.user
            form.save()

            return redirect("homepage:show-crops")
    else:
        form = CropsForm()

    return render(request, "homepage/addcrops.html", {"form": form})


def Update_crops(request, Cid):
    crops = Crops.objects.get(Cid=Cid)
    form = CropsForm(request.POST, instance=crops)

    if form.is_valid():
        form.save()
        return redirect("homepage:show-crops")
    
    else:
        print(form.errors)

    return render(request, "homepage/updatecrops.html", {"crops": crops})


