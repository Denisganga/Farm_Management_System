from django import forms
from .models import Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            "Eid",
            "Name",
            "Country_code",
            "Phone_number",
            "Position",
            "Salary",
            "Performance",
        ]
