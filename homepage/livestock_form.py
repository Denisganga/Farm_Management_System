from django import forms 
from .models import Livestock

class LivestockForm(forms.ModelForm):
    class Meta:
        model= Livestock
        fields=[
            'Tag_number',
            'Animal_type',
            'Age',
            'Breed',
            
                ]