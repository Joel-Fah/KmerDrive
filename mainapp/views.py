from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='website:login')
def mainView(request, username):
    template_name = 'index.html'
    username = str(User.objects.get(username=request.user.username))
    context = {}
    return render(request, template_name, context)

@login_required(login_url='website:login')
def account(request):
    template_name = 'account.html'
    context = {}
    return render(request, template_name, context)