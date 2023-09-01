from django.urls import path
from .views import PDFView

urlpatterns = [
    path('', PDFView.as_view(), name='form_view'),
]
