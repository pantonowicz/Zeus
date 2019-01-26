from django.shortcuts import render
from django.views.generic import ListView, CreateView

from calculation_app.models import Clients


class ClientListView(ListView):
    model = Clients
    template_name = "calculation_app/client_list.html"
    context_object_name = 'clients'


class ClientAddView(CreateView):
    model = Clients
    fields = ['name', 'segment', '']
    template_name = 'calculation_app/add_client.html'


def home(request):
    return render(request, 'calculation_app/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'calculation_app/about.html', {'title': 'About'})
