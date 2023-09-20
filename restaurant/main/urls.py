from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('make_order/', views.make_order, name='make_order'),
    path('delete_order/', views.delete_order, name='delete_order'),
    path('confirmed_delete_order/', views.confirmed_delete_order, name='confirmed_delete_order'),
    path('menu/', views.menu, name='menu'),
]