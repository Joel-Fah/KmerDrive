from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def mainView(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

def account(request):
    template_name = 'account.html'
    context = {}
    return render(request, template_name, context)