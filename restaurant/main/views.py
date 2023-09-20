from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Customer, Establishment, Tables, Dish, Reservation


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
            user_id = request.user.id
            customer = Customer.objects.create(user_id=user_id)
            customer.save()
            user_for_reservation = Reservation.objects.create(user_id=user_id)
            user_for_reservation.save()

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
    id = request.user.id
    customer = Customer.objects.get(user_id=id)
    try:
        reservation = Reservation.objects.get(user_id=id)
    except:
        reservation = None

    return render(request, 'main/profile.html', context={
        'username': username,
        'customer': customer,
        'reservation': reservation,
        })


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
        vegetarian = request.POST.get('vegetarian')
        if new_first_name:
            customer.first_name = new_first_name
        if new_last_name:
            customer.last_name = new_last_name
        if new_adress:    
            customer.adress = new_adress
        if vegetarian:
            if vegetarian == 'No':
                vegetarian = False
            else:
                vegetarian = True
            customer.is_vegetarian = vegetarian
        customer.save()

    return render(request, 'main/edit_profile.html', context={
        'info': customer
    })


@login_required(login_url='/login/')
def make_order(request):
    establishments = Establishment.objects.all()
    dishes = Dish.objects.all()

    if request.method == 'POST':
        user_id = request.user.id
        customer = Customer.objects.get(user_id=user_id)
        user = Reservation.objects.get(user_id=user_id)
        establishment = request.POST.get('establishment')
        establishment = Establishment.objects.get(name=establishment)
        dish = request.POST.get('dish')
        dish = Dish.objects.get(name=dish)
        time = request.POST.get('time')
        free_tables = Tables.objects.exclude(table_is_reserved=True)
        reserved_table = free_tables.first()

        user.establishment = establishment
        user.dish = dish
        user.time = time
        user.table = reserved_table
        user.save()

        reserved_table.table_is_reserved = True
        reserved_table.reservation_time = time
        reserved_table.customer = customer
        reserved_table.save()

    return render(request, 'main/make_order.html', context={
        'establishments': establishments,
        # 'free_tables': free_tables,
        'dishes': dishes
        })


@login_required(login_url='/login/')
def delete_order(request):
    return render(request, 'main/delete_order.html')


@login_required(login_url='/login/')
def confirmed_delete_order(request):
    user_id = request.user.id
    reservation = Reservation.objects.get(user_id=user_id)
    reservation.time = None
    reservation.dish_id = None
    reservation.establishment_id = None
    table_id = reservation.table_id
    table = Tables.objects.get(id=table_id)
    table.table_is_reserved = False
    table.reservation_time = None
    table.customer_id = None
    reservation.table_id = None
    reservation.save()
    table.save()

    return redirect('profile')


class LoginUserView(LoginView):
    template_name = 'main/login.html'
    next_page = 'index'
    redirect_authenticated_user = True


class LogoutUserView(LogoutView):
    next_page = 'index'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'main/change_password.html'
    success_url = '/profile'