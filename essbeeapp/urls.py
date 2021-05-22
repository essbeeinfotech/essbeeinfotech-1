from django.urls import path
from . import views

app_name = 'essbeeapp'

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.ContactView, name='contact'),
    path('about', views.about, name='about'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('news', views.news, name='news'),
    path('chat', views.chat, name='chat'),
    path('clients', views.clients, name='clients'),
    path('blog', views.blog, name='blog'),
    path('<slug:c_slug>/', views.service, name='service'),
    path('news/<slug:n_slug>/', views.latestNews, name='latestNews'),
path('mission', views.mission, name='mission'),





]

