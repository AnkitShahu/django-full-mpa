from django.contrib import admin
from django.http.request import HttpRequest
from .models import Home, Doctor, Contact, OurMission, Services, Faq, SEO, Pages
# Register your models here.

#admin.site.register(Home)

class addhide(admin. ModelAdmin):
    def has_add_permission(self, request):
        return False
#admin.site.register(Contact, addhide)

class contactAdmin(admin.ModelAdmin):
   list_display = ['id','full_name', 'phone_number', 'email' ]
admin.site.register(Contact, contactAdmin)


class faqinline(admin.StackedInline):
    model = Faq
    extra = 0

class serviceadmin(admin.ModelAdmin):
    inlines = [faqinline]

admin.site.register(Services, serviceadmin)

admin.site.register(Faq)

class DoctorAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all":("css/main.css",)
        }
        js = ("js/app.js",)
    
admin.site.register(Doctor, DoctorAdmin)

class OurMissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable the "Add" button
        return False
admin.site.register(OurMission, OurMissionAdmin)

admin.site.register(SEO)
admin.site.register(Pages)        