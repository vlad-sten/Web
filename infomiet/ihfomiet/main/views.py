from django.shortcuts import render, redirect
from .models import UsersPersons
from .forms import UsersPersonsForm

# Create your views here.

def index(request):
    return render(request, 'main/main1.html')


def login(request):
    return render(request, 'main/input.html')


def registration(request):
    if request.method == 'POST':
        form = UsersPersonsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general')
        else:
            error = 'Форма заполнена неверно!'

    form = UsersPersonsForm()

    data = {
        'form': form
    }
    return render(request, 'main/registration.html', data)


def articles(request):
    return render(request, 'general/articles0.html')


def gallery(request):
    return render(request, 'general/gallery0.html')


def links(request):
    return render(request, 'general/links0.html')



