from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


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


class LoginUserView(LoginView):
    template_name = 'main/login.html'
    next_page = 'index'
    redirect_authenticated_user = True


class LogoutUserView(LogoutView):
    next_page = 'index'