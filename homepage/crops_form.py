from django import forms
from .models import Crops,Crop_expenses


class CropsForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = [
            "Cid",
            "Field_name",
            "Field_description",
            "Crop_name",
            "Variety",
            "Planting_date",
            "Harvesting_date",
            "Sales",
            "Sales_description"
        ]

class Crop_expensesForm(forms.ModelForm):
    class Meta:
        model=Crop_expenses
        fields=[
            "Expense_date",
            "Expense_type",
            "Expense_description",
            "Budget",
            "Expense_amount",
            "Supplier",
            "Payment_method",
            "Receipt_number"
        ]
