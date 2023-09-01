# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.views import View
# from xhtml2pdf import pisa
# from io import BytesIO
# from .forms import MyForm

# # Create your views here.
# def forms(request):
#     return render(request, 'forms.html')



# # def form_view(request):
#     # if request.method == 'POST':
#     #     form = MyForm(request.POST)
#     #     if form.is_valid():
#     #         name = form.cleaned_data['name']
#     #         email = form.cleaned_data['email']
#     #         message = form.cleaned_data['message']
            
#     #         context = {
#     #             'name': name,
#     #             'email': email,
#     #             'message': message,
#     #         }
            
#     #         # Render the form data using a template
#     #         html = render(request, 'form_template.html', context).content
            
#     #         # Generate the PDF
#     #         pdf = pdfkit.from_string(html, False)
            
#     #         # Send the generated PDF as a response
#     #         response = HttpResponse(content_type='application/pdf')
#     #         response['Content-Disposition'] = 'attachment; filename="form.pdf"'
#     #         response.write(pdf)
#     #         return response
#     # else:
#     #     form = MyForm()
    
#     # return render(request, 'form.html', {'form': form})
    


# class PDFView(View):
#     def get(self, request):
#         form = MyForm()
#         return render(request, 'form.html', {'form': form})

#     def post(self, request):
#         form = MyForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             context = {
#                 'name': name,
#                 'email': email,
#                 'message': message,
#             }
#             template = get_template('form_template.html')
#             html = template.render(context)
#             pdf_file = self.create_pdf(html)
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="form.pdf"'
#             response.write(pdf_file)
#             return response
#         return render(request, 'form.html', {'form': form})

#     def create_pdf(self, html):
#         pdf_file = BytesIO()
#         pisa.CreatePDF(BytesIO(html.encode('utf-8')), pdf_file)
#         pdf_file.seek(0)
#         return pdf_file



import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from io import BytesIO
from .forms import MyForm
from .models import MyFormsmodel
from PIL import Image
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import requests
import json

class PDFView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST)
        
            # Process the image as needed
        image_data = request.POST.get('imageData', None)
        
        
        if form.is_valid():
            new_pas= form.cleaned_data['new_pas']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            offi_loc = form.cleaned_data['offi_loc']
            sel_pro = form.cleaned_data['sel_pro']
            select_insu = form.cleaned_data['select_insu']
            how_did_you = form.cleaned_data['how_did_you']
            Av_date_best_time = form.cleaned_data['Av_date_best_time']
            Al_date_best_time = form.cleaned_data['Al_date_best_time']
            Avail_date = form.cleaned_data['Avail_date']
            Alter_date = form.cleaned_data['Alter_date']
            insu_mem_id = form.cleaned_data['insu_mem_id']
            insu_grp_id = form.cleaned_data['insu_grp_id']
            
            data_book_app = MyFormsmodel(
                new_pas = new_pas,
                name = name,
                email = email,
                message = message,
                phone = phone,
                offi_loc = offi_loc,
                sel_pro = sel_pro,
                select_insu = select_insu,
                how_did_you = how_did_you,
                Av_date_best_time = Av_date_best_time,
                Al_date_best_time = Al_date_best_time,
                Avail_date = Avail_date,
                Alter_date = Alter_date,
                insu_mem_id = insu_mem_id,
                insu_grp_id = insu_grp_id,
            )
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
            
            data_book_app.save()

            #if image_data:
                # Remove the data URL prefix
                # image_data = image_data.replace('data:image/png;base64,', '')
                # print(image_data)
                # Decode the base64-encoded image data
                # image = Image.open(BytesIO(base64.b64decode(image_data)))
                # print(image)
                
            context = {
                'new_pas': new_pas,
                'name': name,
                'email': email,
                'message': message,
                'phone': phone,
                'offi_loc': offi_loc,
                'sel_pro': sel_pro, 
                'select_insu': select_insu,
                'how_did_you': how_did_you,
                'Avail_date': Avail_date,
                'Av_date_best_time':  Av_date_best_time,
                'Alter_date': Alter_date,
                'Al_date_best_time':  Al_date_best_time,
                'image': image_data,
                'insu_mem_id': insu_mem_id,
                'insu_grp_id': insu_grp_id
            }
            template = get_template('form_template.html')
            html = template.render(context)
            pdf_file = self.create_pdf(html)
            

            #pdf_filename = 'form.pdf'
            #email.attach(pdf_filename, pdf_file.getvalue(), 'application/pdf')

            
            

                    #Sending Email
            subject = 'Thanks For your information we will get back to you soon'
            message =  f'Name: {name} || Email: {email} || Phone Number: {phone} || Meassage: {message} || Office Location: {offi_loc} || Doctor: {offi_loc}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['ankitshahu2023@gmail.com', email_from,]
            #send_mail( subject, message, email_from, recipient_list,  fail_silently=False, )

            
            template = get_template('form_template.html')
            html = template.render(context)
            pdf_file = self.create_pdf(html)
           
           # Attach the PDF to an email using EmailMessage
            email = EmailMessage(
                subject,
                message,
                email_from,
                recipient_list,
            )
            email.attach('form.pdf', pdf_file.getvalue(), 'application/pdf')
            #email.attach_file(pdf_file, 'application/pdf')
            email.send()
            messages.success(request, 'Thanks for the submitting forms! we will get back to you soon ')
          #  response = HttpResponse(content_type='application/pdf')
          #  response['Content-Disposition'] = 'attachment; filename="form.pdf"'
          #  response.write(pdf_file.getvalue())
            return render(request, 'form.html', {'form': form})

        return render(request, 'form.html', {'form': form})

    def create_pdf(self, html):
        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)
        if pisa_status.err:
            raise Exception('PDF generation error')
        pdf_file.seek(0)
        return pdf_file

