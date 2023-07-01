from django.urls import path, include
from . import views
import django.contrib.auth.urls

from .views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('registration', Register.as_views, name='registration')
]
