from django import forms
from .models import Machinery,Machinery_activities

class MachineryForm(forms.ModelForm):
    class Meta:
        model=Machinery
        fields=[
            'Number_plate',
            'Equipment_name',
            'Purchase_price',
            'Purchase_date',
            'Operation',
            'Maintenance_activities'
            
        ]

class Machinery_activitesForm(forms.ModelForm):
    class Meta:
        model=Machinery_activities
        fields=[
            'Activity_date',
            'Activity_type',
            'Activity_cost',
            'Description'
        ]