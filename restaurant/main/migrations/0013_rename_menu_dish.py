# Generated by Django 4.2.5 on 2023-09-19 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_menu_establishment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Dish',
        ),
    ]
