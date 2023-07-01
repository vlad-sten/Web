from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('articles', views.articles, name='articles'),
    path('gallery', views.gallery, name='gallery'),
    path('links', views.links, name='links'),
    path('create', views.create, name='create'),
    path('get_data', views.get_data),
]
