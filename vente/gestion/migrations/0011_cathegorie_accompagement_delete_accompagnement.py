# Generated by Django 4.0.3 on 2022-03-18 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_accompagnement'),
    ]

    operations = [
        migrations.AddField(
            model_name='cathegorie',
            name='accompagement',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.cathegorie'),
        ),
        migrations.DeleteModel(
            name='Accompagnement',
        ),
    ]
