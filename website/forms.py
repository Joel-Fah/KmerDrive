from django import forms
from django.forms.widgets import CheckboxInput, EmailInput, FileInput, NumberInput, PasswordInput, Select, TextInput, Textarea
from .models import ContactInfo
from django import forms
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
                    'aria-describedby' : 'helfpId'
                }
            ),

            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'abc@xyz.com',
                    'aria-describedby' : 'helfpId'
                }
            ),
            
            'phone': TextInput(
                attrs={
                    'name': 'phone',
                    'class': 'form-control',
                    'id': 'phone',
                    'placeholder': 'phone number',
                    'aria-describedby' : 'helfpId'
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
