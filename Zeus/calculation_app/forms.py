from django import forms

from calculation_app.models import Calculation, WasteCodes, MassWaste


class MassWasteAddForm(forms.Form):
    calculation = forms.ModelChoiceField(queryset=Calculation.objects.all())
    waste_code = forms.ModelChoiceField(queryset=WasteCodes.objects.all())
    waste_mass = forms.DecimalField(max_digits=9, decimal_places=2)
