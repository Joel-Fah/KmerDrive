from django.urls import path, include
from .views import mainView

# Creat your urls here.
urlpatterns = [
    path('', mainView, name='app'),
]