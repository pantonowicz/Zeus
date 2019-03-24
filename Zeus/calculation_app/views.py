from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib import messages

from calculation_app.forms import AddClientForm, AddAnnouncementForm, EditAnnouncementForm
from calculation_app.models import Announcements, SalesTeamMember, ValuationTeamMember, Calculation, Client


def test_func(user, role):
    if user.profile.role == role:
        return True
    else:
        return False


class MainView(ListView):
    model = Announcements
    paginate_by = 10
    ordering_by = ['-date']
    template_name = 'calculation_app/main.html'


class SalesPanelView(LoginRequiredMixin, View):
    def get(self, request):
        sales_rep = SalesTeamMember.objects.get(user_id=self.request.user.id)
        clients = sales_rep.client_set.all()
        return render(request, 'calculation_app/client_list.html', locals())

    def test_func(self):
        return test_func(self.request.user, 0)


class ValuationPanelView(LoginRequiredMixin, View):
    def get(self, request):
        valuation_employee = ValuationTeamMember.objects.get(user_id=self.request.user.id)
        evaluation = valuation_employee.evaluation.all()
        return render(request, 'calculation_app/valuation_list.html', locals())

    def test_func(self):
        return test_func(self.request.user, 1)


class CalculationPanelView(LoginRequiredMixin, View):
    def get(self, request):
        calculations = Calculation.objects.all()
        return render(request, 'calculation_app/calculation_list.html', locals())

    def test_func(self):
        return test_func(self.request.user, 2)


class ClientDetailView(LoginRequiredMixin, View):
    def get(self, request, client_id):
        client = get_object_or_404(Client, id=client_id)
        return render(request, 'calculation_app/client_detail.html', locals())


class ClientAddView(LoginRequiredMixin, View):
    def get(self, request):
        sales_rep = SalesTeamMember.objects.get(user_id=self.request.user.id)
        form = AddClientForm(initial={'sales_rep': sales_rep})
        return render(request, 'calculation_app/client_add.html', {'form': form})

    def post(self, request):
        form = AddClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            sales_r = SalesTeamMember.objects.get(user=request.user)
            new_client.sales_rep = sales_r
            new_client.save()
            return redirect('client-list')
        return render(request, 'calculation_app/client_add.html', locals())


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'segment', 'city', 'postal', 'street', 'nip']
    template_name = 'calculation_app/client_update_form.html'
    success_url = reverse_lazy('client-list')


class ClientDeleteView(DetailView):
    model = Client
    template_name = 'calculation_app/client_confirm_delete.html'
    succes_url = reverse_lazy('main')


class AnnouncementsAddView(LoginRequiredMixin, View):
    class_form = AddAnnouncementForm

    def get(self, request):
        form = self.class_form()
        return render(request, 'calculation_app/announcement_add.html', {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            new_announcement = form.save(commit=False)
            new_announcement.author = request.user
            new_announcement.save()
            messages.success(request, 'New announcement added')
            return redirect('main')
        return render(request, 'calculation_app/announcement_add.html', {'form': form})


class AnnouncementsEditView(LoginRequiredMixin, View):
    class_form = EditAnnouncementForm

    def get(self, request, announcement_id):
        announcement = get_object_or_404(Announcements, id=announcement_id)
        form = self.class_form(instance=announcement)
        return render(request, 'calculation_app/announcement_add.html', locals())

    def post(self, request, announcement_id):
        announcement = get_object_or_404(Announcements, id=announcement_id)
        form = self.class_form(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement has been modified!')
            return redirect('main')
        return render(request, 'calculation_app/announcement_add.html', {'form': form})
