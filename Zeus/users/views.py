from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from calculation_app.models import SalesTeamMember, ValuationTeamMember, CalculationTeamMember
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile


class LoginUserView(auth_views.LoginView):
    template_name = "users/login.html"


class LogoutUserView(auth_views.LogoutView):
    template_name = "users/logout.html"


class RegisterUserView(View):

    def get(self, request):
        return render(request, 'users/register_user_role.html')

    def post(self, request):
        button = request.POST.get('button')
        if button == 'sales':
            return redirect('register-sales')
        elif button == 'valuation':
            return redirect('register-valuation')
        elif button == 'calculation':
            return redirect('register-calculation')


class RegisterSalesTeamView(View):

    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = 0
            user.profile.save()
            SalesTeamMember.objects.create(user_id=user.id)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created')
            return redirect('register')
        return render(request, 'users/register.html', {'form': form})


class RegisterValuationTeamView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = 1
            user.profile.save()
            ValuationTeamMember.objects.create(user_id=user.id)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created')
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})


class RegisterCalculationTeamView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = 2
            user.profile.save()
            CalculationTeamMember.objects.create(user_id=user.id)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created')
            return redirect('register')
        return render(request, 'users/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm
        pform = ProfileUpdateForm
        return render(request, 'users/profile.html', locals())

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        button = request.POST.get('button')
        if button == 'update':
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has benn succesfully updated')
                return redirect('profile')
            else:
                if u_form.is_valid():
                    u_form.save()
                    messages.success(request, f'Your account has benn succesfully updated')
        elif button == 'change_password':
            return redirect('change-password')


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'users/user_confirm_password_change.html', locals())

    def post(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = profile.save()
            auth_views.update_session_auth_hash(request, user)
            messages.success(request, "Password has benn changed")
            return redirect('profile')
        else:
            messages.error(request, 'Please type new password')
        return render(request, 'users/user_confirm_password_change.html', locals())
