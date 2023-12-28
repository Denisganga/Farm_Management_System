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
from .models import Crops,Crop_expenses,Crop_sales,Crop_operations
from .crops_form import CropsForm,Crop_expensesForm,Crop_salesForm,Crop_operationsForm


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

def Delete_crops (request,Cid):
    crops=Crops.objects.get(Cid=Cid)
    if request.method =="POST":
        crops.delete()
        return redirect("homepage:show-crops")
    
    return render(request,'homepage/deletecrops.html', {'crops':crops})

def Show_crop_expenses(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)
    expenses=Crop_expenses.objects.filter(crops=crops)

    return render(request,'homepage/showcropexpenses.html',{'crops':crops,'expenses':expenses})

def Add_crop_expenses(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)

    if request.method=='POST':
        form=Crop_expensesForm(request.POST)
        if form.is_valid():
            crop_expense=form.save(commit=False)
            crop_expense.crops=crops
            crop_expense.save()
            return redirect('homepage:show-cropexpenses', Cid=crops.Cid)
        
    else:
        form = Crop_expensesForm()
        return render(request,'homepage/addcropexpenses.html',{'form':form, 'crops':crops})
    

def Update_crop_expenses(request,Cid,Expense_date):
    crops=get_object_or_404(Crops,Cid=Cid)
    crop_expenses=get_object_or_404(Crop_expenses,crops__Cid=Cid,Expense_date=Expense_date)
    form=Crop_expensesForm(request.POST,instance=crop_expenses)

    if form.is_valid():
        form.save()
        return redirect('homepage:show-cropexpenses',Cid=crop_expenses.crops.Cid)
    else:
        print(form.errors)

    return render(request,'homepage/updatecropexpenses.html',{'crops':crops,'crop_expenses':crop_expenses})

def Delete_crop_expenses(request,Cid,Expense_date):
    crop_expenses=get_object_or_404(Crop_expenses, crops__Cid=Cid,Expense_date=Expense_date)
    if request.method=="POST":
        Crop_expenses.delete()
        return redirect('homepage:show-cropexpenses ',Cid=crop_expenses.crops.Cid)
    
    return render(request,'homepage/deletecropexpenses.html',{'crop_expenses':crop_expenses})
    

def Show_crop_sales(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)
    sales=Crop_sales.objects.filter(crops=crops)

    return render(request,"homepage/showcropsales.html",{'crops':crops,'sales':sales})

def Add_crop_sales(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)

    if request.method =='POST':
        form=Crop_salesForm(request.POST)
        if form.is_valid():
            crop_sale=form.save(commit=False)
            crop_sale.crops=crops
            crop_sale.save()
            return redirect('homepage:show-cropsales', Cid=crops.Cid)
        
    else:
        form=Crop_salesForm()
        return render(request,'homepage/addcropsales.html', {'form':form, 'crops':crops})
    

def Delete_crop_sales(request,Cid,Sale_date):
    crop_sales=get_object_or_404(Crop_sales,crops__Cid=Cid,Sale_date=Sale_date)

    if request.method=='POST':
        crop_sales.delete()
        return redirect('homepage:show-cropsales', Cid=crop_sales.crops.Cid)
    return render(request,'homepage/deletecropsales.html',{'crop_sales':crop_sales})

def Update_crop_sales(request,Cid,Sale_date):
    crops= get_object_or_404(Crops,Cid=Cid)
    crop_sales=get_object_or_404(Crop_sales,crops__Cid=Cid,Sale_date=Sale_date)
    form=Crop_salesForm(request.POST,instance=crop_sales)

    if form.is_valid():
        form.save()

        return redirect('homepage:show-cropsales', Cid=crop_sales.crops.Cid)
    
    else:
        print(form.errors)

    return render(request,'homepage/updatecropsales.html',{'crops':crops,'crop_sales':crop_sales})

def Show_crop_operations(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)
    operations=Crop_operations.objects.filter(crops=crops)

    return render(request,'homepage/showcropoperations.html',{'crops':crops, 'operations':operations})

def Add_crop_operations(request,Cid):
    crops=get_object_or_404(Crops,Cid=Cid)

    if request.method=='POST':
        form=Crop_operationsForm(request.POST)
        if form.is_valid():
            crop_operation=form.save(commit=False)
            crop_operation.crops=crops
            crop_operation.save()
            return redirect('homepage:show-cropoperations',Cid=crops.Cid)
    else:
        form=Crop_operationsForm()
        return render(request, 'homepage/addcropoperations.html',{'form':form,'crops':crops})
    

#views for the Machinery

from .models import Machinery
from .machinery_form import MachineryForm

def Show_machinery(request):
    machinery = Machinery.objects.filter(user=request.user)

    return render(request, "homepage/showmachinery.html", {'machinery':machinery})


def Add_machinery(request):
    if request.method=='POST':
        form = MachineryForm(request.POST)
        if form.is_valid():
            machinery= form.save(commit=False)
            machinery.user =request.user
            form.save()
            return redirect("homepage:show-machinery")
        
    else:
        form = MachineryForm()

        return render(request,"homepage/addmachinery.html", {"form":form})


def Delete_machinery(request,Number_plate):
    machinery=Machinery.objects.get(Number_plate=Number_plate)
    if request.method=="POST":
        machinery.delete()
        return redirect("homepage:show-machinery")
        
    return render(request,"homepage/deletemachinery.html", {"machinery":machinery})


def Update_machinery(request,Number_plate):
    machinery=Machinery.objects.get(Number_plate=Number_plate)
    form = MachineryForm(request.POST, instance=machinery)

    if form.is_valid():
        form.save()
        return redirect("homepage:show-machinery")
    
    else:
        print(form.errors)
    
    return render(request, "homepage/updatemachinery.html", {'machinery':machinery})

#view function of the livestock section
from .livestock_form import LivestockForm,Livestock_productionForm
from .models import Livestock,Livestock_production
from django.shortcuts import render, get_object_or_404

def Show_livestock(request):
    livestock = Livestock.objects.filter(user=request.user)

    return render(request,"homepage/showlivestock.html", {'livestock':livestock})


def Add_livestock(request):
    if request.method=="POST":
        form=LivestockForm(request.POST)
        if form.is_valid():
            livestock=form.save(commit=False)
            livestock.user = request.user

            form.save()

            return redirect("homepage:show-livestock")
        
    else:
        form = LivestockForm()
        return render(request,"homepage/addlivestock.html", {'form':form})
    

def Update_livestock(request,Tag_number):
    livestock=Livestock.objects.get(Tag_number=Tag_number)
    form = LivestockForm(request.POST,instance=livestock)

    if form.is_valid():
        form.save()
        return redirect("homepage:show-livestock")
    
    else:
        print(form.errors)

    return render(request,"homepage/updatelivestock.html",{'livestock':livestock})

def Delete_livestock(request,Tag_number):
    livestock=Livestock.objects.get(Tag_number=Tag_number)
    if request.method=="POST":
        livestock.delete()
        return redirect("homepage:show-livestock")
    
    return render(request, "homepage/deletelivestock.html", {'livestock':livestock})

def Show_livestock_production(request, Tag_number):
    livestock = get_object_or_404(Livestock, Tag_number=Tag_number)
    productions = Livestock_production.objects.filter(livestock=livestock)

    return render(request, 'homepage/showlivestockproduction.html', {'livestock': livestock, 'productions': productions})


def Add_livestock_production(request, Tag_number):
    livestock = get_object_or_404(Livestock, Tag_number=Tag_number)

    if request.method == 'POST':
        form = Livestock_productionForm(request.POST)
        if form.is_valid():
            livestock_production = form.save(commit=False)
            livestock_production.livestock = livestock
            livestock_production.save()
            return redirect('homepage:show-livestockproduction', Tag_number=livestock.Tag_number)
    else:
        form = Livestock_productionForm()

        return render(request, 'homepage/addlivestockproduction.html', {'form': form, 'livestock': livestock})
    

def Delete_livestock_production(request,Tag_number,Production_date):
    livestock_production = get_object_or_404(Livestock_production,livestock__Tag_number=Tag_number,Production_date=Production_date)
    if request.method=="POST":
        livestock_production.delete()
        return redirect("homepage:show-livestockproduction",  Tag_number=livestock_production.livestock.Tag_number)
    
    return render(request, 'homepage/deletelivestockproduction.html',{'livestock_production':livestock_production})

def Update_livestock_production(request,Tag_number,Production_date):
    livestock=get_object_or_404(Livestock,Tag_number=Tag_number)
    livestock_production=get_object_or_404(Livestock_production,livestock__Tag_number=Tag_number,Production_date=Production_date)
    form=Livestock_productionForm(request.POST,instance=livestock_production)

    if form.is_valid():
        form.save()
        return redirect('homepage:show-livestockproduction', Tag_number=livestock_production.livestock.Tag_number)
    else:
        print(form.errors)

    return render(request,'homepage/updatelivestockproduction.html',{'livestock':livestock, 'livestock_production':livestock_production})