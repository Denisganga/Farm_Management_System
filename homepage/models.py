from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.core.validators import MaxValueValidator,MinValueValidator

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

class Machinery_maintenance(models.Model):
    machinery=models.ForeignKey(Machinery,on_delete=models.CASCADE)

    Date= models.DateField(help_text="m/d/y")
    Machinery_part=models.CharField(max_length=100)
    Technician_details=models.CharField(max_length=100,blank="True")
    Cost= models.IntegerField()
    Description=models.TextField()

    class Meta:
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

class Milk_production(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)


    Year=models.IntegerField(validators=[MinValueValidator(1)])
    Month=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    Day=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)],default=1)

    Livestock_number=models.IntegerField()
    Morning_production=models.DecimalField(max_digits=10,decimal_places=2,help_text='production in litres')
    Midday_production=models.DecimalField(max_digits=10,decimal_places=2,help_text='production in litres', blank=True)
    Evening_production=models.DecimalField(max_digits=10,decimal_places=2,help_text='production in litres',blank=True)
    Total_production=models.DecimalField(max_digits=10,decimal_places=2,default=0,editable=False)

    Morning_consumption=models.DecimalField(max_digits=10,decimal_places=2,help_text='feed consumed in kg')
    Evening_consumption=models.DecimalField(max_digits=10,decimal_places=2,help_text='feed consumed in kg',blank=True)
    Total_consumption=models.DecimalField(max_digits=10,decimal_places=2,default=0,editable=False)

    def save(self,*args,**kwargs):
        morning_production=float(self.Morning_production)
        midday_production=float(self.Midday_production)
        evening_production=float(self.Evening_production)

        self.Total_production=Decimal(morning_production+midday_production+evening_production)

        morning_consumption=float(self.Morning_consumption)
        evening_consumption=float(self.Evening_consumption)

        self.Total_consumption=Decimal(morning_consumption+evening_consumption)

        super().save(*args,**kwargs)


class Eggs_production(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    Year =models.IntegerField(validators=[MinValueValidator(1)])
    Month = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(12)])
    Day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    Morning_egg_collection=models.DecimalField(max_digits=10,decimal_places=2,help_text='total number of eggs collected')
    Midday_egg_collection=models.DecimalField(max_digits=10,decimal_places=2,help_text='total number of eggs collected', blank=True)
    Evening_egg_collection=models.DecimalField(max_digits=10,decimal_places=2,help_text='total number of eggs collected',blank=True)
    Total_egg_collection=models.DecimalField(max_digits=10,decimal_places=2,default=0,editable=False)

    Morning_feeds=models.DecimalField(max_digits=10,decimal_places=2,help_text='feed consumed in kg')
    Evening_feeds=models.DecimalField(max_digits=10,decimal_places=2,help_text='feed consumed in kg',blank=True)
    Total_feeds=models.DecimalField(max_digits=10,decimal_places=2,default=0,editable=False)

    def save(self,*args, **kwargs):
        morning_egg_collection=float(self.Morning_egg_collection)
        midday_egg_collection=float(self.Midday_egg_collection)
        evening_egg_collection=float(self.Evening_egg_collection)

        self.Total_egg_collection=Decimal(morning_egg_collection+midday_egg_collection+evening_egg_collection)

        morning_feeds=float(self.Morning_feeds)
        evening_feeds=float(self.Evening_feeds)

        self.Total_feeds=Decimal(morning_feeds+evening_feeds)
        
        super().save(*args, **kwargs)





