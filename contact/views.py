from django.shortcuts import render
from .models import Contact

# Create your views here.
def ContactView(request):
    if request.method == 'POST':
        name=request.POST['name']
        from_email=request.POST['from_email']
        mobile=request.POST['mobile']
        message=request.POST['message']
        contact = Contact(name=name,mobile=mobile,from_email=from_email, message=message)
        contact.save()
        return render(request, 'index.html', {"name": name})


