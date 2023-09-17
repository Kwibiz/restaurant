from django.contrib import admin


from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'adress']
    search_fields = ['first_name', 'last_name', 'adress']

admin.site.register(Customer, CustomerAdmin)


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'has_vegetarian_dishes']
    search_fields = ['name']

admin.site.register(Establishment, EstablishmentAdmin)


class TablesAdmin(admin.ModelAdmin):
    list_display = [
        'establishment', 
        'table_number', 
        'table_is_reserved', 
        'customer', 
        'reservaion_time'
        ]

admin.site.register(Tables, TablesAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'establishment',
        'dish',
        'ingredients',
        'description',
        'is_vegetarian'
    ]

admin.site.register(Menu, MenuAdmin)