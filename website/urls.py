from django.urls import path
from .views import HomeView, ContactView, RegisterView, user_login, user_logout

# Creat your urls here.
app_name = 'website'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]