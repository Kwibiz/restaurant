# Generated by Django 4.2.5 on 2023-09-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_reservaion_time_tables_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
