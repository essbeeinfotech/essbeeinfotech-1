from django.contrib import admin
from .models import Service
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'img','desc']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Service,ServiceAdmin)