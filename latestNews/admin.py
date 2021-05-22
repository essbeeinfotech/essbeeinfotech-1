from django.contrib import admin
from .models import LatestNews
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['heading', 'slug', 'img','sub_heading']

    prepopulated_fields = {'slug': ('heading',)}

admin.site.register(LatestNews,NewsAdmin)