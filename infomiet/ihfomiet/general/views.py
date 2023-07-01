from django.shortcuts import render, redirect
from .models import Articles, Like
from .forms import ArticlesForm, LikeForm
import hashlib
import re

from django.http import JsonResponse
import requests
import json


def general(request):
    return render(request, 'general/general.html')


def articles(request):
    articles = Articles.objects.all()
    return render(request, 'general/articles.html', {'articles': articles})


def articles0(request):
    articles = Articles.objects.all()
    return render(request, 'general/articles0.html', {'articles': articles})


def gallery(request):
    try:
        likes = Like.objects.all()
    except:
        likes = []
    data = {'like_amount': len(likes)}

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save()

    try:
        likes = Like.objects.all()
    except:
        likes = []
    data = {'like_amount': len(likes), 'form': LikeForm()}
    return render(request, 'general/gallery.html', data)


def links(request):
    return render(request, 'general/links.html')


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = 'Форма заполнена неверно!'

    form = ArticlesForm()

    data = {
        'form': form
    }
    return render(request, 'general/create.html', data)


def get_data(request):
    likes = Like.objects.all()
    data = {"like_amount": len(likes)}
    return JsonResponse(data, safe=False)
