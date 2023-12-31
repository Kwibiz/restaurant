# Generated by Django 4.2.5 on 2023-09-17 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customer_is_vegetarian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=80)),
                ('has_vegetarian_dishes', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=30)),
                ('ingredients', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('establishment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.establishment')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='has_reservation',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_is_reserved', models.BooleanField(default=False)),
                ('reservaion_time', models.DateTimeField(blank=True)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customer')),
                ('establishment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.establishment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
                ('table', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.tables')),
            ],
        ),
    ]
