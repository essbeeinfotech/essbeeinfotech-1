from django.shortcuts import render
from .models import Service
# Create your views here.
def service(request):

    result=Service.objects.all()
    print(result)

    return render(request,'index.html',{'results':result})
