# Generated by Django 4.0.3 on 2022-03-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_article_description_article_origine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='origine',
            field=models.CharField(default='/', max_length=15),
        ),
    ]
