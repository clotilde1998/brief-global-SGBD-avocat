# Generated by Django 4.0 on 2022-01-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avocatsApp', '0003_alter_clients_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiers',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
    ]
