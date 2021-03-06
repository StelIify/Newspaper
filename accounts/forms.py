from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms


class CustomUserCreatingForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'age', 'password1', 'password2')


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'image')
