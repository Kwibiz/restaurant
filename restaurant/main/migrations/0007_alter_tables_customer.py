# Generated by Django 4.2.5 on 2023-09-17 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_tables_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customer'),
        ),
    ]