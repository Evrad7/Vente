# Generated by Django 4.0.3 on 2022-03-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_alter_article_origine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accompagnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=15, null=True)),
                ('cathegorie', models.ManyToManyField(to='gestion.cathegorie')),
            ],
        ),
    ]
