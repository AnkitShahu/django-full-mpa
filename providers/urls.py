from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider, name='provider'),
    path('<slug:slug>/', views.pdetails, name='post_detail'),
]