from django.shortcuts import render
from .models import Testimonials
# Create your views here.
def TestimonialsView(request):
    test=Testimonials.objects.all()

    return render(request,'index.html',{'test':test})
