# Generated by Django 4.2 on 2025-02-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_badge_title_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_table', models.IntegerField(verbose_name='Номер таблицы')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок категории')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('au', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('ag', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Прейскурант',
                'verbose_name_plural': 'Прейскурант',
            },
        ),
    ]
