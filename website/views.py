from django.core.mail.message import BadHeaderError
from django.shortcuts import redirect, render, HttpResponse
from .models import ContactInfo
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.html import format_html
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

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
            return redirect('contact')
        else:
            form = ContactForm()

    context = {
        'nbar' : 'contact',
        'modelform': ContactForm
    }
    return render(request, template_name, context)
