# Generated by Django 4.2 on 2025-02-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='name',
        ),
        migrations.RemoveField(
            model_name='price',
            name='num_table',
        ),
        migrations.AlterField(
            model_name='price',
            name='ag',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ag'),
        ),
        migrations.AlterField(
            model_name='price',
            name='au',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='au'),
        ),
    ]
