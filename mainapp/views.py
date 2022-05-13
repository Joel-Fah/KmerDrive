from multiprocessing import context
from multiprocessing.sharedctypes import Value
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.contrib import messages
from mainapp.models import ProfileInfo
from .forms import ProfileForm

# Create your views here.

class ActionsView(View):
    
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        pk = get_object_or_404(User, id=self.kwargs["pk"])
        user = get_object_or_404(User, username=self.kwargs["user"])
        context = {
            'nbar': 'actions',
            'pk': pk,
            'user': user
        }
        return render(request, self.template_name, context)

class ProfileView(View):
    template_name = "account.html"
    form_class = ProfileForm
    
    def get(self, request, *args, **kwargs):
        pk =get_object_or_404(User, id=self.kwargs["pk"])
        user = get_object_or_404(User, username=self.kwargs["user"])
        context = {
            'nbar': 'account',
            'pk': pk,
            'user': user
        }
        return render(request, self.template_name, context)
    
class UpdateProfileView(UpdateView):
    model = ProfileInfo
    fields = ['image', 'bio']
    template_name_suffix = '_update_form'
    success_url = '/'