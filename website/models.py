from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    '''Manages the contact form'''

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        error_messages={'required': ("Name must be provided.")})

    email = models.EmailField(
        null=True,
        blank=True,
        error_messages={'required': ("Email must be provided")})

    phone = models.CharField(
        max_length=9,
        null=False,
        blank=False,
        error_messages={'required':("Phone number must be provided.")})

    message = models.TextField(
        null=False,
        blank=False,
        error_messages={'required': ("A valid message must be provided.")}
    )

    def __str__(self):
        return self.name + ' ' + self.email
