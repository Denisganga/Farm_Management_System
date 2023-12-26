from django import forms
from .models import Crops,Crop_expenses,Crop_sales


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

class Crop_salesForm(forms.ModelForm):
    class Meta:
        model=Crop_sales
        fields=[
            'Sale_date',
            'Quantity_sold',
            'Unit_price',
            'Buyer_information',
            'Payment_method',
            'Payment_status',
            'Invoice_number',
            'Additional_notes'
        ]
