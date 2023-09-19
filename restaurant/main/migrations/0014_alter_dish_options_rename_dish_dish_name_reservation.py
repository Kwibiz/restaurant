# Generated by Django 4.2.5 on 2023-09-19 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_rename_menu_dish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'Dishes'},
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dish')),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.establishment')),
                ('table', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.tables')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
