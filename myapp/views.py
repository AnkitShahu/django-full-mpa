from django.shortcuts import render
from .models import Home, Doctor, Contact, OurMission, SEO
from django.contrib import messages
import requests
import json
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    books = Home.objects.all()
    doc = Doctor.objects.all()
    mission = OurMission.objects.all()
    seo_detail = SEO.objects.filter(page__page__iexact='Home').first()
    context = {"book": books, "doc": doc, "mission": mission, "seo_detail" :seo_detail}
    return render(request, "index.html", context)

def about(request):
    doc = Doctor.objects.all()
    seo_detail = SEO.objects.filter(page__page__iexact='About').first()
    context = {"doc": doc, "seo_detail" :seo_detail}
    return render(request, "about.html", context)

# def services(request):
#     return render(request, "services.html")


def contact(request):
    seo_detail = SEO.objects.filter(page__page__iexact='Contact').first()
    context = {"seo_detail" :seo_detail}
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        office_location = request.POST.get('office_location')
        doctor = request.POST.get('doctor')

        contact = Contact(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
            office_location=office_location,
            doctor=doctor
        )
        
        print(contact)
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LfbPMQmAAAAAJW08AAS64GAP20fextsF-fxF2GS'
        cature = {
            'secret': secretkey,
            'sitekey': clientkey
        }
        print(cature)
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=cature)
        response = json.loads(r.text)
        verify = response['success']
        print('this is verify',verify)
        contact.save()
        
        #Sending Email
        subject = 'Thanks For your information we will get back to you soon'
        message =  f'Name: {full_name} || Email: {email} || Phone Number: {phone_number} || Meassage: {message} || Office Location: {office_location} || Doctor: {doctor}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['svaidyamhc@gmail.com', email,]
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request, 'Thanks You! we will get back you as soon as posible')
    else:
        # Handle successful form submission (e.g., redirect)
        # return redirect('success')
        #messages.error(request,'Please fill in all the fields correctly!')
         pass
    return render(request, 'contact.html', context)

def privacy_page(request):
    seo_detail = SEO.objects.filter(page__page__iexact='Privacy').first()
    context = {"seo_detail" :seo_detail}
    return render(request, "privacy.html", context)

def team(request):
    return render(request, "team.html")
    
def testimonials(request):
    return render(request, 'testimonials.html')
    
    
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ankitshahu2023@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'testimonials.html')