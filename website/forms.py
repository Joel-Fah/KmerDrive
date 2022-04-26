from django import forms
from django.forms.widgets import EmailInput, NumberInput, TextInput, Textarea
from .models import ContactInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms below.
class ContactForm(forms.ModelForm):
    # Meta data
    class Meta:
        model  = ContactInfo
        fields = [
            'name',
            'email',
            'phone',
            'message'
        ]

        # Definition of widgets
        widgets = {
            'name': TextInput(
                attrs={
                    'name': 'name',
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'First & Last Names',
                    'aria-describedby': 'helpId'
                }
            ),

            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Your email address',
                    'aria-describedby': 'helpId'
                }
            ),
            
            'phone': NumberInput(
                attrs={
                    'name': 'phone',
                    'class': 'form-control',
                    'id': 'phone',
                    'placeholder': 'phone number',
                    'aria-describedby': 'helpId'
                }
            ),


            'message': Textarea(
                attrs={
                    'name': 'message',
                    'rows': '8',
                    'class': 'form-control',
                    'placeholder': 'Tell us about ...',
                }
            ),
        }