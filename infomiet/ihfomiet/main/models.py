from django.db import models


class UsersPersons(models.Model):
    surname = models.CharField('Фамилия', max_length=64)
    name = models.CharField('Имя', max_length=64)
    middle_name = models.CharField('Отчество', max_length=64)
    mail = models.EmailField('Почта', max_length=64)
    password = models.CharField('Пароль', max_length=64)

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
