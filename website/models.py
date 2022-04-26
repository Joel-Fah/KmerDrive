from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    '''Manages the contact form/page'''
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        error_messages={'required': ("Provide a first and last name.")})
    
    email = models.EmailField(
        null=True,
        blank=True,
        error_messages={'required': ("Provide an email address.")})
    
    phone = models.CharField(max_length=9,
                             null=False,
                             blank=False,
                             error_messages={'required':("Provide a valid phone number")})
    
    message = models.TextField(
        null=False,
        blank=False,
        error_messages={'required': ("You must say something.")})

    def __str__(self):
        return self.name + ' ' + self.email