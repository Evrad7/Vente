# Generated by Django 4.0.4 on 2022-08-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0017_rename_type_articles_panier_types_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(default='fdsfqffds', max_length=254),
        ),
    ]
