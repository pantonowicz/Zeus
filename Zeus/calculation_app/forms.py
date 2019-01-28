from django import forms

from calculation_app.models import MassWaste


class MassWasteAddForm(forms.ModelForm):
    class Meta:
        model = MassWaste
        fields = ['waste_codes', 'waste_mass']
