from django import forms 
from .models import Livestock, Livestock_production

class LivestockForm(forms.ModelForm):
    class Meta:
        model= Livestock
        fields=[
            'Tag_number',
            'Animal_type',
            'Age',
            'Breed',


            
                ]

class Livestock_productionForm(forms.ModelForm):
    class MEta:
        model=Livestock_production
        fields=[
            'Production_date',
            'Production_amount',
            'Feed_consumed',
            'Comments'
        ]