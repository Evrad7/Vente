# Generated by Django 4.0.3 on 2022-03-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_phototypearticle_remove_typearticle_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default='fsdf', upload_to='image_article'),
            preserve_default=False,
        ),
    ]
