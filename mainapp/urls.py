from django.urls import path, include
from .views import mainView, account

# Creat your urls here.
app_name = 'mainapp'

urlpatterns = [
    path('', mainView, name='app'),
    path('account/', account, name='account'),
]