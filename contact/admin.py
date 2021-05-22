from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_email', 'mobile_num', 'message','date']
    list_filter = ['date']
    search_fields = ['name']
