from django.urls import path
from .views import auth, home, contact

# Creat your urls here.
urlpatterns = [
    path('auth/', auth, name='auth'),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]