# Generated by Django 4.2 on 2025-02-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_callbackrequest_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequest',
            name='message',
            field=models.TextField(max_length=2000, verbose_name='Сообщение'),
        ),
    ]
