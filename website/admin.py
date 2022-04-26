from django.contrib import admin
from .models import ContactInfo

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    search_fields = ['name']

admin.site.register(ContactInfo, ContactAdmin)