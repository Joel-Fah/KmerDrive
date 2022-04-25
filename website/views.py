from django.shortcuts import render

# Create your views here.

def home(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = 'contact.html'
    context = {}
    return render(request, template_name, context)