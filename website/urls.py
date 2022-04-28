from django.urls import path
from .views import home, contact, register, user_login, user_logout

# Creat your urls here.
app_name = 'website'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]