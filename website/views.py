from django.shortcuts import redirect, render
from .forms import ContactForm
from django.contrib import messages
from django.utils.html import format_html

# Create your views here.

def home(request):
    template_name = 'home.html'
    context = {}
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

            # Test if form data was saved and output corresponding flash message to confirm message placement or not.
            try:
                form.save()
                message_out_success = format_html(
                    f'Thanks for contacting us, <strong> {name} </strong> ! Your message has been sent successfully. We will get to you as soon as possible at <strong> {email} </strong> !'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Sorry, <strong> {name} </strong> ! There was a problem sending your message. Please reload and try again!'
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
        'modelform': ContactForm
    }
    return render(request, template_name, context)
