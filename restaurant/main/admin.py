from django.contrib import admin


from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'adress']
    search_fields = ['first_name', 'last_name', 'adress']


admin.site.register(Customer, CustomerAdmin)