from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Login',
            'first_name': 'First Name',
            'last_name': 'Last name',
            'email': 'email'
        }
        help_texts = {
            'username': 'Type your login',
            'first_name': 'Type your first name',
            'last_name': 'Type your last name',
            'email': 'Type your email'
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        labels = {
            'email': 'email'
        }
        help_texts = {
            'email': 'Type new email'
        }


class ProfileUpdateForm(forms.ModelForm):
    model = Profile
    fields = ['image']
    labels = {
        'image': 'image'
    }
    help_text = {
        'image': 'Add new profile image'
    }
