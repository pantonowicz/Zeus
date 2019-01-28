from django import forms

from calculation_app.models import MassWaste, WasteCodes, Calculation


class WasteCodeAddForm(forms.Form):
    waste_codes = forms.ModelChoiceField(queryset=WasteCodes.objects.all())
    waste_mass = forms.DecimalField(max_digits=9, decimal_places=2)
