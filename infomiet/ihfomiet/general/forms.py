from .models import Articles, Like
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'author', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Название статьи',
                'name': 'title'
            }),
            "author": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Автор',
                'name': 'author'
            }),
            "full_text": Textarea(attrs={
                'class': 'form_input',
                'placeholder': 'Текст статьи'
            }),
        }


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = []
