from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreatingForm, CustomUserLoginForm, UserUpdateForm
from django.contrib.auth import views as auth_views


class SignUpView(CreateView):
    form_class = CustomUserCreatingForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginView(auth_views.LoginView):
    form_class = CustomUserLoginForm
    template_name = 'registration/login.html'


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, template_name='accounts/profile.html', context=context)



