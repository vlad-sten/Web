from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('articles0', views.articles, name='articles0'),
   path('gallery0', views.gallery, name='gallery0'),
   path('links0', views.links, name='links0'),
   path('input', views.login, name='login'),
   path('registration', views.registration, name='registration')
]
