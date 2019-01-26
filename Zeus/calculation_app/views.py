from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from calculation_app.models import Clients


class ClientListView(ListView):
    model = Clients
    template_name = "calculation_app/client_list.html"
    context_object_name = 'clients'


class ClientAddView(CreateView):
    model = Clients
    fields = ['name', 'segment', 'city', 'postal', 'street', 'nip']
    template_name = 'calculation_app/add_client.html'
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


def home(request):
    return render(request, 'calculation_app/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'calculation_app/about.html', {'title': 'About'})
