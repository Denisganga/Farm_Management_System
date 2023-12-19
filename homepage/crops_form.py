from django import forms
from .models import Crops


class CropsForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = [
            "Cid",
            "Field_name",
            "Field_description",
            "Crop_name",
            "Planting_date",
            "Harvesting_date",
            "Expenses",
            "Expenses_description",
            "Sales",
        ]
