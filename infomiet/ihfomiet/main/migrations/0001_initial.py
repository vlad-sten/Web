# Generated by Django 4.2.1 on 2023-06-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=64, verbose_name='Отчество')),
                ('mail', models.EmailField(max_length=64, verbose_name='Почта')),
                ('password', models.CharField(max_length=64, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
