# Generated by Django 4.2 on 2025-01-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_weddingrings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingrings',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/weddingrings/%Y/%m/', verbose_name='Фото'),
        ),
    ]
