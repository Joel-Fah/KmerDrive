from django import forms
from django.forms import ModelForm
from .models import ProfileInfo
from django.forms.widgets import TextInput, FileInput, Textarea

# Create your forms here.
class ProfileForm(ModelForm):
    class Meta:
        model = ProfileInfo
        fields = [
            'image',
            'bio'
        ]
        
        widgets = {
            'image': FileInput(
                attrs={
                    'name': 'image',
                    'id': 'image',
                    'class': 'form-control',
                    'placeholder': 'Select a profile image',
                    'aria-describedby': 'helpId'
                }
            ),
            
            'bio': Textarea(
                attrs={
                    'name': 'bio',
                    'id': 'bio',
                    'rows': '3',
                    'class': 'form-control',
                    'placeholder': 'A small phrase about you ...',
                }
            ),
        }