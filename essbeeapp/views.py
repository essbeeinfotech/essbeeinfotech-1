from django.shortcuts import render, redirect

from essbee.settings import EMAIL_HOST_USER
from service.models import Service
from blog.models import Blog
from Testimonials.models import Testimonials
from contact.models import Contact
from ourwork.models import Ourwork
from latestNews.models import LatestNews
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib import messages
import json


# Create your views here.
def index(request):
    test = Testimonials.objects.all()[:3]
    result = Service.objects.all()[:9]
    blog = Blog.objects.all()[:3]
    work = Ourwork.objects.all()[:6]

    return render(request, 'index.html', {'results': result, 'blog': blog, 'test': test, 'work': work})


def ContactView(request):
    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['from_email']
        mobile_num = request.POST['mobile_num']
        message = request.POST['message']

        # ''' Begin reCAPTCHA validation '''

        captcha_token = request.POST.get('g-recaptcha-response')
        cap_url = 'https://www.google.com/recaptcha/api/siteverify'
        cap_secret = '6Lfnoc8aAAAAAGf3VbYh4gVBMX8nhuMmkc6TpvTs'
        cap_data = {'secret': cap_secret, 'response': captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        # ''' End reCAPTCHA validation '''

        if cap_json['success'] == True:
            contact = Contact(name=name, mobile_num=mobile_num, from_email=from_email, message=message)
            contact.save()
            if name and from_email:
                try:
                    send_mail('Essbee Infotech',
                              'Thank you for getting in touch! We appreciate you contacting us. One of our colleagues will get back in touch with you soon!Have a great day!',
                              EMAIL_HOST_USER, [from_email,'ajaymol@essbeeinfotech.com'],fail_silently=False)
                    print("mail send")
                    messages.info(request, "Thank you for contacting us.")

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.info(request, "invalid entry.")




        else:

            messages.error(request, "Invalid Captcha, Try Again")
            return redirect('/')



        work = Ourwork.objects.all()[:6]
        test = Testimonials.objects.all()
        result = Service.objects.all()[:6]
        blog = Blog.objects.all()[:3]

        return render(request, 'index.html',
                      {'name': name, 'results': result, 'blog': blog, 'test': test, 'work': work})


def about(request):
    return render(request, 'include/about.html', {})


def privacy_policy(request):
    return render(request, 'include/privacy_policy.html', {})


def contactUs(request):
    return render(request, 'include/contactUs.html', {})


def chat(request):
    return render(request, 'include/live_chat.html', {})


def clients(request):
    work = Ourwork.objects.all()[:12]
    return render(request, 'include/clients.html', {'work': work})


def blog(request):
    blog = Blog.objects.all()[:4]
    blogs = Blog.objects.all()[:1]
    return render(request, 'include/blog.html', {'blog': blog, 'blogs': blogs})


def service(request, c_slug):
    result = Service.objects.get(slug=c_slug)
    # result=None
    return render(request, 'include/service.html', {'results': result})


def news(request):
    newss = LatestNews.objects.all()[:12]
    return render(request, 'include/news.html', {'newss': newss})


def latestNews(request, n_slug):
    news = LatestNews.objects.get(slug=n_slug)
    return render(request, 'include/LatestNews.html', {'news': news})


def mission(request):
    return render(request, 'include/mission.html', {})



