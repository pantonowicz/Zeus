from django import forms

from calculation_app.models import MassWaste


class WasteCodeAddForm(forms.ModelForm):
    class Meta:
        model = MassWaste
        fields = ['waste_codes', 'waste_mass']
        labels = {
            'waste_codes': 'Waste Codes',
            'waste_mass': 'Waste Mass',
        }
