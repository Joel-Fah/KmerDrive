from django.shortcuts import render

# Create your views here.

def mainView(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)