from django.urls import path, include
from .views import home

# Creat your urls here.
urlpatterns = [
    path('', home, name='home'),
]