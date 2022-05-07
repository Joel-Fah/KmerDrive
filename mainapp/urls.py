from re import A
from django.urls import path
from .views import ActionsView, ProfileView, UpdateProfileView
from django.contrib.auth.decorators import login_required

# Creat your urls here.
app_name = 'mainapp'

urlpatterns = [
    path('<str:pk>/<str:user>/', login_required(ActionsView.as_view()), name='app'),
    path('<str:pk>/<str:user>/account/', login_required(ProfileView.as_view()), name='account'),
    path('<str:pk>/<str:user>/account/update/', login_required(UpdateProfileView.as_view()), name='update'),
]