from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Services, Faq, SEO

# Create your views here.
def services(request):
    servicess = Services.objects.all()
    seo_detail = SEO.objects.filter(page__page__iexact='Services').first()
    return render(request, "sindex.html", {"ser": servicess, "seo_detail" :seo_detail})

def sdetails(request, slug):
    Servicess = Services.objects.all()
    service = Services.objects.get(slug= slug)
    faqs = Faq.objects.filter(category= service)
    print(faqs)
    ser = get_object_or_404(Servicess, slug=slug)
    services = {"ser": ser, "faqs": faqs, "allser": Servicess}
    return render(request, "sdetail.html", services)