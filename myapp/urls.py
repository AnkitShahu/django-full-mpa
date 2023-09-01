from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='conatact'),
    #path('provider/', views.provider, name='provider')
    path('privacy-policy/', views.privacy_page, name='privacy_page'),
    path('terms-and-conditions/', views.team, name='termsandconditions'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('email/', views.email, name='email'),
    
]
