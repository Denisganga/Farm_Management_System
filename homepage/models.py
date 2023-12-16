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
        db_table="employees"



