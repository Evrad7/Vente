# Generated by Django 4.0.4 on 2022-08-11 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0018_article_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='email',
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default='fdsfqffds'),
        ),
    ]
