# Generated by Django 4.0 on 2022-01-26 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avocatsApp', '0006_alter_dossiers_clients_alter_dossiers_personnels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiers',
            name='clients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avocatsApp.clients'),
        ),
    ]
