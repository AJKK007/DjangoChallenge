from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='first-home'),
    path('about/', views.about, name='first-about'),
    path('how-it-works/', views.howitworks, name='first-how-it-works'),
    path('contact/', views.contact, name='first-contact')
]