from django.db import models
from django.contrib.auth.models import User

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
    Expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Expenses_description = models.TextField(blank=True)
    Sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Sales_description = models.TextField(blank=True)

    def calculate_profit(self):
        if self.Harvesting_date and self.Sales:
            expenses_total = self.Expenses
            return self.Sales - expenses_total
        else:
            return None
        
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
    Production_date=models.DateField()
    Production_amount=models.CharField(max_length=20)
    Feed_consumed=models.DecimalField(max_digits=10,decimal_places=2,help_text='field consumed in kg')
    Comments=models.TextField(null=True,blank=True)


