# Generated by Django 4.0.3 on 2022-04-17 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0016_remove_panier_articles_panier_type_articles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panier',
            old_name='type_articles',
            new_name='types_articles',
        ),
    ]