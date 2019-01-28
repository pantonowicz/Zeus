from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from calculation_app.forms import WasteCodeAddForm, CalculationAddForm
from calculation_app.models import Clients, Subcontractors, Calculation, MassWaste


# --------------------------------CLIENTS----------------------------------------
class ClientListView(ListView):
    model = Clients
    template_name = "calculation_app/client_list.html"
    context_object_name = 'clients'


class ClientAddView(CreateView):
    model = Clients
    fields = ['name', 'segment', 'city', 'postal', 'street', 'nip']
    template_name = 'calculation_app/client_add.html'
    success_url = reverse_lazy('client-list')


class ClientDetailView(DetailView):
    model = Clients
    template_name = 'calculation_app/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Clients
    fields = '__all__'
    success_url = reverse_lazy('client-list')
    template_name = 'calculation_app/client_update_form.html'


class ClientDeleteView(DeleteView):
    model = Clients
    template_name = 'calculation_app/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')


# ----------------------------SUBCONTRACTORS--------------------------------------
class SubcontractorListView(ListView):
    model = Subcontractors
    template_name = 'calculation_app/subcontractor_list.html'
    context_object_name = 'subcontractors'


class SubcontractorAddView(CreateView):
    model = Subcontractors
    fields = '__all__'
    template_name = 'calculation_app/subcontractor_add.html'
    success_url = reverse_lazy('subcontractor-list')


class SubcontractorDetailView(DetailView):
    model = Subcontractors
    template_name = 'calculation_app/subcontractor_detail.html'


class SubcontractorUpdateView(UpdateView):
    model = Subcontractors
    fields = '__all__'
    success_url = reverse_lazy('subcontractor-list')
    template_name = 'calculation_app/subcontractor_update_form.html'


class SubcontractorDeleteView(DeleteView):
    model = Subcontractors
    template_name = 'calculation_app/subcontractor_confirm_delete.html'
    success_url = reverse_lazy('subcontractor-list')


# ----------------------------Calculations--------------------------------------
class CalculationAddView(CreateView):
    model = Calculation
    fields = ['contract_duration', 'payment_deadline', 'offer_deadline', 'client']
    template_name = 'calculation_app/calculation_add.html'
    success_url = reverse_lazy('calculation-list')


class CalculationListView(ListView):
    model = Calculation
    template_name = 'calculation_app/calculation_list.html'


class CalculationDetailView(DetailView):
    model = Calculation
    template_name = 'calculation_app/calculation_detail.html'


class CalculationUpdateView(UpdateView):
    model = Calculation
    fields = ['contract_duration', 'payment_deadline', 'offer_deadline']
    success_url = reverse_lazy('calculation-list')
    template_name = 'calculation_app/calculation_update_form.html'


class CalculationDeleteView(DeleteView):
    model = Calculation
    template_name = 'calculation_app/calculation_confirm_delete.html'
    success_url = reverse_lazy('calculation-list')


class CalculationCodeAddView(View):

    def get(self, request, pk):
        calculation = get_object_or_404(Calculation, pk=pk)
        form = WasteCodeAddForm()
        return render(request, 'calculation_app/calculation_detail.html', locals())

    def post(self, request, pk):
        calculation = Calculation.objects.get(pk=pk)
        form = WasteCodeAddForm(request.POST, instance=calculation)
        if form.is_valid():
            calculation_id = form.cleaned_data.get('pk')
            w_code = form.cleaned_data.get('waste_codes')
            w_mass = form.cleaned_data.get('waste_mass')
            new_code = MassWaste()
            new_code.calculation_id = pk
            new_code.waste_codes_id = w_code
            new_code.waste_mass_id = w_mass
            new_code.save()
            return redirect('calculation-detail', locals())


# ------------------------------------------------------------------------------------


def home(request):
    return render(request, 'calculation_app/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'calculation_app/about.html', {'title': 'About'})
