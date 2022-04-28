from django.core.mail.message import BadHeaderError
from django.shortcuts import redirect, render, HttpResponse
from .models import ContactInfo
from .forms import ContactForm, CreateUserForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.html import format_html
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    template_name = 'register.html'
    
    if request.user.is_authenticated:
        return redirect('website:home')
    else:
        registerForm = CreateUserForm
        
        if request.method  == 'POST':
            registerForm = CreateUserForm(request.POST)
            if registerForm.is_valid():
                username = registerForm.cleaned_data.get('username')
                
                # Test if form data was saved and output corresponding flash message to confirm message placement or not.
                try:
                    registerForm.save()
                    message_out_success = format_html(
                        f'Registration successful! Now log into your account.'
                    )
                    messages.success(
                        request,
                        message_out_success
                    )
                except:
                    msg = """
                    Registration failed! Please try again. If the problem persists, <a href='{url}'>Contact us</a>
                    """
                    url = reverse('contact')
                    message_out_error = format_html(msg)
                    messages.error(
                        request,
                        mark_safe(message_out_error.format(url=url))
                    )
                
                # Redirect to mainapp
                return redirect('website:login')
        context = {
            'registerForm': registerForm
        }
        
        return render(request, template_name, context)
    
def user_login(request):
    template_name = 'login.html'
    if request.user.is_authenticated:
        return redirect('website:home')
    else:
        if request.method  == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                message_out_success = format_html(
                    f'You are successfully logged in as <strong>{username}</strong>!'
                )
                messages.success(
                    request,
                    message_out_success
                )
                return redirect('mainapp:app')
            else:
                messages.error(
                    request,
                    f'Login failed! Incorrect username or password.'
                )
                return redirect('website:login')
            
        return render(request, template_name)

def user_logout(request):
    logout(request)
    messages.info(
        request,
        f'You are now loggged out.'
    )
    return redirect('website:login')

def home(request):
    template_name = 'home.html'
    context = {
        'nbar' : 'home',
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'contact.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            emailSubject = f'{name} <{email}>'

            # Uncomment this later to send email to required address
            try:
                send_mail(
                    emailSubject, #subject
                    message, #message
                    email, #from email
                    ['joelfah2003@gmail.com'], #to email
                    fail_silently=False
                    )
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            # Test if form data was saved and output corresponding flash message to confirm message placement or not.
            try:
                form.save()
                message_out_success = format_html(
                    f'Thanks for contacting us, <strong> {name} </strong> ! Your message has been sent successfully. We will get to you at <strong> {email} </strong> in the meantime.'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Sorry, <strong> {name} </strong> ! There was a problem sending your message. Please try again to fill the form!'
                )
                messages.error(
                    request,
                    message_out_error
                )
            
            # Redidrect to the same page with message output.
            return redirect('website:contact')
        else:
            form = ContactForm()

    context = {
        'nbar' : 'contact',
        'modelform': ContactForm
    }
    return render(request, template_name, context)
