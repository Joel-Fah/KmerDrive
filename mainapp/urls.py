from django.urls import path
from .views import mainView, account

# Creat your urls here.
app_name = 'mainapp'

urlpatterns = [
    path('<str:username>/', mainView, name='app'),
    path('account/', account, name='account'),
]