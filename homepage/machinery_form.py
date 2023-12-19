from django import forms
from .models import Machinery

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