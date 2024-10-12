from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("aboutpage/", about_page, name='about'),
    path('contactpage/', contact_page, name= 'contact' ),
]
