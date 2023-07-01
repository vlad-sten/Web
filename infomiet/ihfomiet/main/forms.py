from .models import UsersPersons
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.mixins import LoginRequiredMixin


class UsersPersonsForm(ModelForm):
    class Meta:
        model = UsersPersons
        fields = ['surname', 'name', 'middle_name', 'mail', 'password', 'password']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Фамилия',
                'name': 'surname',
                'pattern': '[А-Я]+[а-я]{1,}'
            }),
            "name": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Имя',
                'name': 'name',
                'pattern': '[А-Я]+[а-я]{1,}'
            }),
            "middle_name": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Отчество',
                'name': 'surname',
                'pattern': '[А-Я]+[а-я]{1,}'
            }),
            "mail": EmailInput(attrs={
                'class': 'form_input',
                'placeholder': 'Эл. почта',
                'name': 'mail',
                'pattern': '[a-z]+@+[a-z]+.+[a-z]'
            }),
            "password": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Пароль',
                'name': 'password',
                'minlength': '8'
            }),
            "repeat_password": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Пароль',
                'name': 'password',
                'minlength': '8'
            })
        }

