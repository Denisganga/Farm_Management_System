from django import forms 
from .models import Livestock, Livestock_production,Milk_production,Eggs_production

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
    class Meta:
        model=Livestock_production
        fields=[
            'Production_date',
            'Production_amount',
            'Feed_consumed',
            'Comments'
        ]

class Milk_productionForm(forms.ModelForm):
    class Meta:
        model=Milk_production

        fields=[
            'Year',
            'Month',
            'Day',
            'Livestock_number',
            'Morning_production',
            'Midday_production',
            'Evening_production',
            'Morning_consumption',
            'Evening_consumption'
        ]

class Egg_productionForm(forms.ModelForm):
    class Meta:
        model=Eggs_production

        fields=[
            'Year',
            'Month',
            'Day',
            'Poultry_number',
            'Morning_egg_collection',
            'Midday_egg_collection',
            'Evening_egg_collection',
            'Morning_feeds',
            'Evening_feeds',
            'Comments'
        ]