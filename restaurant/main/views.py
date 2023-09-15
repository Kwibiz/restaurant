from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Customer


def index(request):
    return render(request, 'main/index.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    
    else:
        form = UserCreationForm()

    return render(request, 'main/registration.html', context={
        'form': form,
    })


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    username = request.user.username

    return render(request, 'main/profile.html', context={'username':username})


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            return redirect('profile')
    return render(request, 'main/change_password.html')


@login_required(login_url='/login/')
def edit_profile(request):
    id = request.user.id
    customer = Customer.objects.get(user_id=id)
    if request.method == 'POST':
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_adress = request.POST.get('adress')
        customer.first_name = new_first_name
        customer.last_name = new_last_name
        customer.adress = new_adress
        customer.save()

    return render(request, 'main/edit_profile.html', context={
        'info': customer
    })


class LoginUserView(LoginView):
    template_name = 'main/login.html'
    next_page = 'index'
    redirect_authenticated_user = True


class LogoutUserView(LogoutView):
    next_page = 'index'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'main/change_password.html'
    success_url = '/profile'