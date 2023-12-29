from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.


class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    Eid = models.IntegerField(primary_key=True, default=0)
    Name = models.CharField(max_length=50)
    Country_code = models.CharField(max_length=4)
    Phone_number = models.CharField(max_length=9)
    Position = models.CharField(max_length=10)
    Salary = models.IntegerField()
    Performance = models.CharField(max_length=10)

    class Meta:
        db_table = "employees"


class Crops(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    Cid = models.IntegerField(primary_key=True, default=0)
    Field_name = models.CharField(max_length=50)
    Field_description = models.TextField()
    Crop_name = models.CharField(max_length=50)
    Variety = models.CharField(max_length=20)
    Planting_date = models.DateField()
    Is_harvested = models.BooleanField(default=False)
    Harvesting_date = models.DateField(null=True, blank=True)

    def calculate_profit(self):
        if self.Harvesting_date and self.Sales:
            expenses_total = self.Expenses
            return self.Sales - expenses_total
        else:
            return None
        
class Crop_expenses(models.Model):
    crops=models.ForeignKey(Crops,on_delete=models.CASCADE)

    Expense_date=models.DateField(help_text='m/d/y')
    Expense_type=models.CharField(max_length=20)
    Expense_description=models.TextField()
    Budget= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    Expense_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    Supplier=models.CharField(max_length=20)
    Payment_method=models.CharField(max_length=10)
    Receipt_number=models.CharField(max_length=20)

    class Meta:
        db_table="Crop_expenses"


class Crop_sales(models.Model):
    crops=models.ForeignKey(Crops,on_delete=models.CASCADE)

    Sale_date=models.DateField(help_text='m/d/y')
    Quantity_sold=models.CharField(max_length=20)
    Unit_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    Total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0,editable=False)
    Buyer_information=models.TextField()
    Payment_method=models.CharField(max_length=20)
    Payment_status=models.CharField(max_length=20, choices=[('pending', 'Pending'), ('received', 'Received')])
    Invoice_number=models.CharField(max_length=20)
    Additional_notes=models.TextField(blank=True)


#lets over ride the save method in order before saving it calculates the total amount


    def save(self, *args, **kwargs):
        # Convert Decimal values to float for multiplication
        quantity_sold = float(self.Quantity_sold)
        unit_price = float(self.Unit_price)

            # Calculate total sale amount before saving
        self.Total_price = Decimal(quantity_sold * unit_price)
        super().save(*args, **kwargs) #here we are calling the initial save 

class Crop_operations(models.Model):
    crops=models.ForeignKey(Crops,on_delete=models.CASCADE)

    Operation_date=models.DateField(help_text="m/d/y")
    Operation_name=models.CharField(max_length=20)
    Additional_notes=models.TextField(blank=True)

    class Meta:
        db_table="Crop_operations"

    

        
class Machinery(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    Number_plate= models.CharField(max_length=20, primary_key=True)
    Equipment_name= models.CharField(max_length=20)
    Purchase_price= models.DecimalField(max_digits=10,decimal_places=2, default=0)
    Purchase_date = models.DateField()
    Operation=models.TextField(blank=True)
    Maintenance_activities= models.TextField(blank=True)

    class Meta:
        db_table = "Machinery"

class Machinery_activities(models.Model):
    machinery= models.ForeignKey(Machinery,on_delete=models.CASCADE)

    Activity_date=models.DateField(help_text="m/d/y")
    Activity_type=models.CharField(max_length=20)
    Activity_cost=models.IntegerField(blank=True)
    Description=models.TextField(blank=True)

    class meta:
        db_table="Machinery_activities"

class Livestock(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    Tag_number = models.CharField(max_length=20, primary_key=True)
    Animal_type= models.CharField(max_length=20)
    Age= models.IntegerField()
    Breed= models.CharField(max_length=20)

    class Meta:
        db_table = "Livestock"

    

class Livestock_production(models.Model):
    livestock=models.ForeignKey(Livestock,on_delete=models.CASCADE)
    Production_date=models.DateField(help_text='m/d/y')
    Production_amount=models.CharField(max_length=20)
    Feed_consumed=models.DecimalField(max_digits=10,decimal_places=2,help_text='field consumed in kg')
    Comments=models.TextField(null=True,blank=True)

    class Meta:
        db_table="Livestock_production"


