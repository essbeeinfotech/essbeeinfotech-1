from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogView(request):
    blog=Blog.objects.all()
    return render(request, 'index.html', {'blog': blog})

