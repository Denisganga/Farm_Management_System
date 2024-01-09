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

def Delete_crop_operations(request,Cid,Operation_date):
    crop_operations=get_object_or_404(Crop_operations,crops__Cid=Cid,Operation_date=Operation_date)
    if request.method=='POST':
        crop_operations.delete()
        return redirect('homepage:show-cropoperations',Cid=crop_operations.crops.Cid)
    
    return render(request, 'homepage/deletecropoperations.html',{'crop_operations':crop_operations})


def Update_crop_operations(request,Cid,Operation_date):
    crops= get_object_or_404(Crops,Cid=Cid)
    crop_operations=get_object_or_404(Crop_operations,crops__Cid=Cid,Operation_date=Operation_date)
    form  = Crop_operationsForm(request.POST,instance=crop_operations)

    if form.is_valid():
        form.save()

        return redirect('homepage:show-cropoperations',Cid=crop_operations.crops.Cid)
    
    return render(request,'homepage/updatecropoperations.html',{'crops':crops,'crop_operations':crop_operations})
    
    
    

#views for the Machinery

from .models import Machinery,Machinery_activities,Machinery_maintenance
from .machinery_form import MachineryForm,Machinery_activitesForm,Machinery_maintenanceForm

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


def Show_machinery_activities(request,Number_plate):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)
    activities=Machinery_activities.objects.filter(machinery=machinery)
    return render(request, 'homepage/showmachineryactivities.html',{'machinery':machinery,'activities':activities})

def Add_machinery_activities(request,Number_plate):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)

    if request.method=='POST':
        form=Machinery_activitesForm(request.POST)
        if form.is_valid():
            machinery_activity=form.save(commit=False)
            machinery_activity.machinery=machinery
            machinery_activity.save()
            return redirect('homepage:show-machineryactivities', Number_plate=machinery.Number_plate)
        

    else:
        form=Machinery_activitesForm()
    return render(request, 'homepage/addmachineryactivities.html',{'machinery':machinery,'form':form})

def Delete_machinery_activity(request,Number_plate,Activity_date):
    machinery_activities=get_object_or_404(Machinery_activities,machinery__Number_plate=Number_plate,Activity_date=Activity_date)
    if request.method=='POST':
        machinery_activities.delete()
        return redirect('homepage:show-machineryactivities',Number_plate=machinery_activities.machinery.Number_plate)
    
    return render(request,'homepage/deletemachineryactivities.html',{'machinery_activities':machinery_activities})


def Update_machinery_activities(request,Number_plate,Activity_date):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)
    machinery_activities=get_object_or_404(Machinery_activities,machinery__Number_plate=Number_plate,Activity_date=Activity_date)
    form=Machinery_activitesForm(request.POST,instance=machinery_activities)

    if form.is_valid():
        form.save()
        return redirect('homepage:show-machineryactivities',Number_plate=machinery_activities.machinery.Number_plate)
    
    return render(request,'homepage/updatemachineryactivities.html',{'machinery':machinery,'machinery_activities':machinery_activities})

def Show_machinery_maintenance(request,Number_plate):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)
    maintenance=Machinery_maintenance.objects.filter(machinery=machinery)
    return render(request,'homepage/showmachinerymaintenance.html',{'machinery':machinery,'maintenance':maintenance})

def Add_machinery_maintenance(request,Number_plate):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)

    if request.method=='POST':
        form=Machinery_maintenanceForm(request.POST)
        if form.is_valid():
            machinery_maintenance=form.save(commit=False)
            machinery_maintenance.machinery=machinery
            machinery_maintenance.save()
            return redirect('homepage:show-machinerymaintenance',Number_plate=machinery.Number_plate)
        
    else:
        form=Machinery_maintenanceForm()
    return render(request, 'homepage/addmachinerymaintenance.html',{'machinery':machinery,'form':form})

def Delete_machinery_maintenance(request,Number_plate,Date):
    machinery_maintenance=get_object_or_404(Machinery_maintenance,machinery__Number_plate=Number_plate,Date=Date)
    if request.method=='POST':
        machinery_maintenance.delete()
        return redirect('homepage:show-machinerymaintenance',Number_plate=machinery_maintenance.machinery.Number_plate)
    
    return render(request,'homepage/deletemachinerymaintenance.html',{'machinery_maintenance':machinery_maintenance})


def Update_machinery_maintenance(request,Number_plate,Date):
    machinery=get_object_or_404(Machinery,Number_plate=Number_plate)
    machinery_maintenance=get_object_or_404(Machinery_maintenance,machinery__Number_plate=Number_plate,Date=Date)
    form=Machinery_maintenanceForm(request.POST,instance=machinery_maintenance)

    if form.is_valid():
        form.save()
        return redirect('homepage:show-machinerymaintenance',Number_plate=machinery_maintenance.machinery.Number_plate)
    
    return render(request,'homepage/updatemachinerymaintenance.html',{'machinery':machinery,'machinery_maintenance':machinery_maintenance})
    


#view function of the livestock section
from .livestock_form import LivestockForm,Livestock_productionForm,Milk_productionForm,Egg_productionForm
from .models import Livestock,Livestock_production,Milk_production,Eggs_production
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



# the milk production section in the dashboard

def Select_year_month(request):
    if request.method=='POST':
        selected_year=request.POST.get('Year')
        selected_month=request.POST.get('Month')
        return redirect('homepage:milk-productionbymonth',selected_year=selected_year,selected_month=selected_month)
    return render(request,'homepage/selectyearmonth.html')

# views.py
import matplotlib
matplotlib.use('Agg') #rendering the graphs that does not use tikinter in order to remove the tikinter error
import matplotlib.pyplot as plt
from io import BytesIO # create an in-memory buffer to temporarily store the binary data of the generated plots.
import base64 # encode the binary data of the plots into Base64 format(Base64 encoding used to convert binary data into  such as images, into a text-based format that can be easily embedded in HTML)

def Milk_production_by_month(request, selected_year, selected_month):
    # Fetching milk production by the year and month selected
    milk_production_records = Milk_production.objects.filter(Year=selected_year, Month=selected_month)

    # Prepare data for the bar graph of total consumption vs day
    days = [record.Day for record in milk_production_records]
    total_consumption = [record.Total_consumption for record in milk_production_records]

    # Create a bar graph for Total Consumption vs Day
    plt.figure(figsize=(12, 6))
    plt.bar(days, total_consumption, color='green')
    plt.title('Total Consumption vs Day')
    plt.xlabel('Day')
    plt.ylabel('Total Consumption')
    
    # Save the plot to a BytesIO object
    image_stream_consumption = BytesIO()
    plt.savefig(image_stream_consumption, format='png')
    image_stream_consumption.seek(0)
    image_base64_consumption = base64.b64encode(image_stream_consumption.read()).decode('utf-8')

    # Close the plot to free up resources
    plt.close()

    # Prepare data for the bar graph of milk production vs day
    total_production = [record.Total_production for record in milk_production_records]

    # Create a bar graph for Milk Production vs Day
    plt.figure(figsize=(12, 6))
    plt.bar(days, total_production, color='blue')
    plt.title('Milk Production vs Day')
    plt.xlabel('Day')
    plt.ylabel('Milk Production')

    # Save the plot to a BytesIO object
    image_stream_production = BytesIO()
    plt.savefig(image_stream_production, format='png')
    image_stream_production.seek(0)
    image_base64_production = base64.b64encode(image_stream_production.read()).decode('utf-8')

    # Close the plot to free up resources
    plt.close()

    # Pass both base64-encoded images to the template
    return render(request, 'homepage/milkproductionbymonth.html', {
        'selected_year': selected_year,
        'selected_month': selected_month,
        'image_base64_consumption': image_base64_consumption,
        'image_base64_production': image_base64_production,
        'milk_production_records': milk_production_records,
    })


def Add_milk_production_by_month(request,selected_year,selected_month):
    if request.method=='POST':
        form=Milk_productionForm(request.POST)
        if form.is_valid():
            production=form.save(commit=False)
            production.Year=selected_year
            production.Month=selected_month
            production.save()
            return redirect('homepage:milk-productionbymonth',selected_year=selected_year,selected_month=selected_month)

    else:
        form=Milk_productionForm()

    return render(request,'homepage/addmilkproduction.html',{'form':form,'selected_year':selected_year,'selected_month':selected_month})



def Delete_milk_production_by_month(request,selected_year,selected_month,Day):
    milk_production_records=get_object_or_404(Milk_production,Day=Day)
    if request.method=='POST':
        milk_production_records.delete()
        return redirect('homepage:milk-productionbymonth', selected_year=selected_year,selected_month=selected_month)
    
    return render(request, 'homepage/deletemilkproduction.html', {'milk_production_records':milk_production_records,'selected_year':selected_year,'selected_month':selected_month})

def Update_milk_production_by_month(request,selected_year,selected_month,Day):
    milk_production_record=get_object_or_404(Milk_production,Day=Day,Year=selected_year,Month=selected_month)
    form=Milk_productionForm(request.POST,instance=milk_production_record)

    if form.is_valid():
        form.save()
        return redirect('homepage:milk-productionbymonth', selected_year=selected_year,selected_month=selected_month)
    
    else:
        print(form.errors)

    return render(request,'homepage/updatemilkproduction.html',{'milk_production_record':milk_production_record, 'selected_year':selected_year,'selected_month':selected_month})

#Eggs production
def Select_year_month_egg(request):
    if request.method=='POST':
        selected_year=request.POST.get('Year')
        selected_month=request.POST.get('Month')
        
    return render('homepage/selcting yearandmonth.html' )

