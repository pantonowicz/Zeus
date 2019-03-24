from django import forms

# # from django.core.exceptions import ValidationError
#
# from calculation_app.models import Calculation, WasteCodes, Subcontractors, UNIT_CHOICES, Order
#
#
# class MassWasteAddForm(forms.Form):
#     calculation = forms.ModelChoiceField(queryset=Calculation.objects.all())
#     waste_code = forms.ModelChoiceField(queryset=WasteCodes.objects.all())
#     waste_mass = forms.DecimalField(max_digits=9, decimal_places=2)
#
#
# class CostAddToCodeForm(forms.Form):
#     subcontractor = forms.ModelChoiceField(queryset=Subcontractors.objects.all())
#     logistic_details = forms.CharField(widget=forms.Textarea)
#     quality_details = forms.CharField(widget=forms.Textarea)
#     unit = forms.ChoiceField(choices=UNIT_CHOICES, widget=forms.Select)
#     local_transport_cost = forms.DecimalField(max_digits=9, decimal_places=2)
#     instalation_transport_cost = forms.DecimalField(max_digits=9, decimal_places=2)
#     management_cost = forms.DecimalField(max_digits=9, decimal_places=2)
from calculation_app.models import Client, Announcements


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('sales_rep',)
        # fields = '__all__'


class AddAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Content',
        }
        help_texts = {
            'title': 'Add annoucement title',
            'text': 'Add annoucement content'
        }


class EditAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'text', 'deleted']
        labels = {
            'title': 'Title',
            'text': 'Text',
            'deleted': 'Select as deleted'
        }
        help_texts = {
            'title': 'Change annoucement title',
            'text': 'Change annoucement content',
        }
