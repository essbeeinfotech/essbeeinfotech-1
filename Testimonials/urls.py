from django.urls import path
from .import views
app_name= 'Testimonials'

urlpatterns = [

    path('Testimonials',views.TestimonialsView,name='Testimonials'),
]